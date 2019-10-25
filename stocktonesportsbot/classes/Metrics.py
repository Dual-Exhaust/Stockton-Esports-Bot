# date_heatmap and date_heatmap_demo are from an answer on stackoverflow
# here: https://stackoverflow.com/questions/32485907/matplotlib-and-numpy-create-a-calendar-heatmap/51977000#51977000
# by user cbarrick
# we updated it slightly to work with the most current pandas version and changed some of the parameters around to work
# better with discord
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import discord
DAYS = ['Sun.', 'Mon.', 'Tues.', 'Wed.', 'Thurs.', 'Fri.', 'Sat.']
MONTHS = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June', 'July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']


def date_heatmap(series, start=None, end=None, mean=False, ax=None, **kwargs):
    '''Plot a calendar heatmap given a datetime series.

    Arguments:
        series (pd.Series):
            A series of numeric values with a datetime index. Values occurring
            on the same day are combined by sum.
        start (Any):
            The first day to be considered in the plot. The value can be
            anything accepted by :func:`pandas.to_datetime`. The default is the
            earliest date in the data.
        end (Any):
            The last day to be considered in the plot. The value can be
            anything accepted by :func:`pandas.to_datetime`. The default is the
            latest date in the data.
        mean (bool):
            Combine values occurring on the same day by mean instead of sum.
        ax (matplotlib.Axes or None):
            The axes on which to draw the heatmap. The default is the current
            axes in the :module:`~matplotlib.pyplot` API.
        **kwargs:
            Forwarded to :meth:`~matplotlib.Axes.pcolormesh` for drawing the
            heatmap.

    Returns:
        matplotlib.collections.Axes:
            The axes on which the heatmap was drawn. This is set as the current
            axes in the `~matplotlib.pyplot` API.
    '''
    # Combine values occurring on the same day.
    dates = series.index.floor('D')
    group = series.groupby(dates)
    series = group.mean() if mean else group.sum()

    # Parse start/end, defaulting to the min/max of the index.
    start = pd.to_datetime(start or series.index.min())
    end = pd.to_datetime(end or series.index.max())

    # We use [start, end) as a half-open interval below.
    end += np.timedelta64(1, 'D')

    # Get the previous/following Sunday to start/end.
    # Pandas and numpy day-of-week conventions are Monday=0 and Sunday=6.
    start_sun = start - np.timedelta64((start.dayofweek + 1) % 7, 'D')
    end_sun = end + np.timedelta64(7 - end.dayofweek - 1, 'D')

    # Create the heatmap and track ticks.
    num_weeks = (end_sun - start_sun).days // 7
    heatmap = np.zeros((7, num_weeks))
    ticks = {}  # week number -> month name
    for week in range(num_weeks):
        for day in range(7):
            date = start_sun + np.timedelta64(7 * week + day, 'D')
            if date.day == 1:
                ticks[week] = MONTHS[date.month - 1]
            if date.dayofyear == 1:
                ticks[week] += f'\n{date.year}'
            if start <= date < end:
                heatmap[day, week] = series.get(date, 0)

    # Get the coordinates, offset by 0.5 to align the ticks.
    y = np.arange(8) - .5
    x = np.arange(num_weeks + 1) - 0.5

    # Plot the heatmap. Prefer pcolormesh over imshow so that the figure can be
    # vectorized when saved to a compatible format. We must invert the axis for
    # pcolormesh, but not for imshow, so that it reads top-bottom, left-right.
    ax = ax or plt.gca()
    mesh = ax.pcolormesh(x, y, heatmap, **kwargs)
    ax.invert_yaxis()

    # Set the ticks.
    ax.set_xticks(list(ticks.keys()))
    ax.set_xticklabels(list(ticks.values()))
    ax.set_yticks(np.arange(8) - .5)
    ax.set_yticklabels(DAYS)

    # Set the current image and axes in the pyplot API.
    plt.sca(ax)
    plt.sci(mesh)

    return ax


def create_date_heatmap(data, date_range, colors, intensity):
    '''An example for `date_heatmap`.

    Most of the sizes here are chosen arbitrarily to look nice with 1yr of
    data. You may need to fiddle with the numbers to look right on other data.
    '''
    # Get some data, a series of values with datetime index.
    data.index = date_range

    # Create the figure. For the aspect ratio, one year is 7 days by 53 weeks.
    # We widen it further to account for the tick labels and color bar.
    figsize = plt.figaspect(7 / 65)
    fig = plt.figure(figsize=figsize)

    # Plot the heatmap with a color bar.
    ax = date_heatmap(data, edgecolor='black')
    plt.colorbar(ticks=range(intensity), pad=0.02)

    # Use a discrete color map with 5 colors (the data ranges from 0 to 4).
    # Extending the color limits by 0.5 aligns the ticks in the color bar.
    cmap = mpl.cm.get_cmap(colors, intensity)
    plt.set_cmap(cmap)
    plt.clim(0, intensity)

    # Force the cells to be square. If this is set, the size of the color bar
    # may look weird compared to the size of the heatmap. That can be corrected
    # by the aspect ratio of the figure or scale of the color bar.
    ax.set_aspect('equal')

    # Save to a file. For embedding in a LaTeX doc, consider the PGF backend.
    # http://sbillaudelle.de/2015/02/23/seamlessly-embedding-matplotlib-output-into-latex.html
    fig.savefig('heatmap.png', bbox_inches='tight')

    # The figure must be explicitly closed if it was not shown.
    plt.close(fig)


def server_joined_data(date_range, players):
    date_list = []
    for day in date_range:
        date_list.append(str(day).split()[0])

    date_count = [0] * len(date_list)
# for each person in the server we get the date they joined and split it so it is just the day stamp
    for guy in players:
        temp_date = guy.joined_at
        time = str(temp_date).split()[0]
        # if the day stamp is in the the list of total days then increase that dates count by one
        if time in date_list:
            # date_list.index returns the index the time is found in so it increases the parallel arrays count at the
            # correct spot
            date_count[date_list.index(time)] += 1

    return pd.Series(date_count, index=date_list)


def tweeted_date_data(date_range, tw):
    date_list = []
    for day in date_range:
        date_list.append(str(day).split()[0])

    date_count = [0] * len(date_list)

    for tweet in tw.tweet_dates():
        temp_date = str(tweet).split()[0]
        time = str(temp_date).split()[0]

        if time in date_list:
            date_count[date_list.index(time)] += 1

    return pd.Series(date_count, index=date_list)


def server_roles(players):

    mpl.style.use('seaborn')

    # total members in the server
    print("There are " + str(len(players)) + " members in the server.")

    # Tallies up date joined by day
    date_list = []
    date_count = []
    for guy in players:
        temp_date = guy.joined_at
        time = str(temp_date).split()[0]
        if time not in date_list:
            date_list.append(time)
            date_count.append(1)
        else:
            date_count[date_list.index(time)] += 1

    x_pos = np.arange(len(date_list))

    plt.yticks(np.arange(min(date_count), max(date_count) + 1, 1.0), fontsize=6)
    plt.xlim(0, 96)
    plt.xticks(x_pos, date_list, fontsize=3)
    plt.xticks(rotation=90)

    plt.plot(date_count)

    plt.savefig('stats.pdf', bbox_inches='tight')


async def get_user_msg_count(channels):
    # Create two parallel arrays to store users and their message counts
    people = []
    count = []
    for channel in channels:
        # If its a text channel, channels can be a few different types
        if isinstance(channel, discord.channel.TextChannel):
            # Creates a list containing every message from a specific channel
            msgs = await channel.history(limit=5000).flatten()
            # Goes through every message in the channel
            for message in msgs:
                # If author hasn't been recorded yet then add them on and make their count start at 1
                if str(message.author) not in people:
                    people.append(str(message.author))
                    count.append(1)
                # If they are already in the list we get their index in the list and increase their count by 1
                else:
                    count[people.index(str(message.author))] += 1
            # Not sure if this actually does anything but I haven't tested without it yet and it works as is
            # Supposed to set the msgs back to nothing before we move on to the next channel
            msgs = []

    return pd.Series(count, index=people)


