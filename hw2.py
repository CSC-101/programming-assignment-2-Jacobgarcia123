import data

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(point1: data.Point, point2: data.Point) -> data.Rectangle:
    #top left
    #bottom right
    tl_x = min(point1.x,point2.x)
    tl_y = max(point1.y,point2.y)
    br_x = max(point1.x,point2.x)
    br_y = min(point1.y,point2.y)

    tl = data.Point(tl_x,tl_y)
    br = data.Point(br_x,br_y)

    return data.Rectangle(tl,br)



# Part 2
def shorter_duration_than(song1,song2) -> bool:
    total_seconds1 = song1.minutes * 60 + song1.seconds
    total_seconds2 = song2.minutes * 60 + song2.seconds

    return total_seconds1 < total_seconds2



# Part 3
def songs_shorter_than (songs:list,max_duration) -> list:
    short_songs = []

    for song in songs:
        songs_seconds = song.duration.minutes * 60 + song.duration.seconds
        max_seconds = max_duration.minutes * 60 + max_duration.seconds

        if songs_seconds < max_seconds:
            short_songs.append(song)

    return short_songs



# Part 4
def running_time(songs:list[data.Song], playlist: list[int] ) -> data.Duration:
    total_m = 0
    total_s = 0

    for song_index in playlist:
        if 0 <= song_index < len(songs):
            song = songs[song_index]
            total_m += song.duration.minutes
            total_s += song.duration.seconds

    total_m += total_s // 60
    total_s = total_s % 60

    return data.Duration(total_m, total_s )


# Part 5
def validate_route(city_links: list[list[str]], route: list[str]) -> bool:

    if len(route) <= 1:
        return True

    links = set()
    for link in city_links:
        if len(link) == 2:
            links.add((link[0], link[1]))
            links.add((link[1], link[0]))

    for i in range(len(route) - 1):
        if (route[i], route[i + 1]) not in links:
            return False

    return True



# Part 6
def longest_repetition(nums:list[int]):
    if not nums:
        return None
    max_length = 1
    current_length = 1
    longest_start_index = 0

    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                longest_start_index = i - current_length
            current_length = 1

    if current_length > max_length:
        longest_start_index = len(nums) - current_length

    return longest_start_index