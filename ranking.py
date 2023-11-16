import requests

def sort_json_list(json_list, key_to_sort, n, ascending):
    
    sorted_data = sorted(json_list, key=lambda x: x[key_to_sort], reverse=ascending)
    result = {}
    
    for course_offering in sorted_data:
        instructor = course_offering['instructor']
        if instructor in result or instructor == "UNKNOWN, INSTRUCTOR":
            continue
        result[instructor] = course_offering

    if len(result) < n:
        return result
    return result[-n:]
