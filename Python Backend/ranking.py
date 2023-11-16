import requests
import RMP_queries.py

#sort list of dictionaries from representing course offering stats. in past 2 years
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


#sorts list of professor objects based on tags
def get_top_professors_for_tag(prof_list : list, key_to_sort, n, ascending) :

    result_list = [] #list of prof dicts than can be passed into helper
    for prof in prof_list:
        prof_tags_dict = prof.get_tag_freq()
        result_list.append(prof_tags_dict)
        
    return sort_json_list(json_list, key_to_sort, n, ascending)
        
    
