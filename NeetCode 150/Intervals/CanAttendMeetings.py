def canAttendMeetings(intervals):
  intervals.sort(key=lambda x: x[0])

  for i in range(1, len(intervals)):
    if intervals[i][0] < intervals[i - 1][1]:
      return False

  return True

print(canAttendMeetings([[2,10],[9,12],[6,9],[13,15]]))