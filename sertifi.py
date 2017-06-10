import requests
import heapq
#import json

response = requests.get('http://apitest.sertifi.net/api/Students')
#print(response)
data = response.json()

#print(data)

year_with_highest_attendance = {}
year_with_highest_overall_gpa = {}
top_10_students_with_highest_overall_gpa = []
student_with_largest_difference_between_max_and_min_gpa = []

for entry in data:
    Name = entry['Name']
    GPARecord = entry['GPARecord']
    max_gpa = max(GPARecord)
    min_gpa = min(GPARecord)
    StartYear = entry['StartYear']
    EndYear = entry['EndYear']
    Id = entry['Id']

    idx = 0
    for x in range(StartYear, (EndYear+1)):
        if x in year_with_highest_overall_gpa:
            year_with_highest_attendance[x] += 1
        else:
            year_with_highest_attendance[x] = 1
    
        if x in year_with_highest_overall_gpa:
            year_with_highest_overall_gpa[x]['count'] += 1
            year_with_highest_overall_gpa[x]['gpa'] += GPARecord[idx]
            idx += 1
        else:
            year_with_highest_overall_gpa[x] = {}
            year_with_highest_overall_gpa[x]['count'] = 1
            year_with_highest_overall_gpa[x]['gpa'] = GPARecord[idx]
            idx += 1
    #student_with_largest_difference_between_max_and_min_gpa[Name] = (max_gpa-min_gpa)
    heapq.heappush(student_with_largest_difference_between_max_and_min_gpa, (-(max_gpa - min_gpa), Id))
    heapq.heappush(top_10_students_with_highest_overall_gpa, (-(sum(GPARecord)/len(GPARecord)), Id))

top_10 = []
for i in range(10):
    top_10.append(heapq.heappop(top_10_students_with_highest_overall_gpa)[1])

max_attendance_year = 0
max_attendance_val = 0
for each_key in year_with_highest_attendance:
    if year_with_highest_attendance[each_key] > max_attendance_val:
        max_attendance_year = each_key
        max_attendance_val = year_with_highest_attendance[each_key]
    elif year_with_highest_attendance[each_key] == max_attendance_val and each_key < max_attendance_year:
        max_attendance_year = each_key
        max_attendance_val = year_with_highest_attendance[each_key]

max_overall_gpa_year = 0
max_overall_gpa_val = 0
for each_key in year_with_highest_overall_gpa:
    gpa_val_year = year_with_highest_overall_gpa[each_key]['gpa']/year_with_highest_overall_gpa[each_key]['count']
    if gpa_val_year > max_overall_gpa_val:
        max_overall_gpa_year = each_key
        max_overall_gpa_val = gpa_val_year



print(max_attendance_year)
print(max_overall_gpa_year)
print(top_10)
most_inconsistent = heapq.heappop(student_with_largest_difference_between_max_and_min_gpa)[1]
print(most_inconsistent)

checkout = {
    "YourName": "Arjun A Kumar",
    "YourEmail": "arjunak1868@gmail.com",
    "YearWithHighestAttendance": max_attendance_year,
    "YearWithHighestOverallGpa": max_overall_gpa_year,
    "Top10StudentIdsWithHighestGpa": top_10,
    "StudentIdMostInconsistent": most_inconsistent
}

#json_obj=json.dumps(checkout)
url = 'http://apitest.sertifi.net/api/StudentAggregate'
headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
r = requests.put(url, data = checkout, headers=headers)
print(r)

