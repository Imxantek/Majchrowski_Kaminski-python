def most_active_session(uid_dict: dict[str, list]):
    most_inquiries = 0
    longest_session_uid = ""
    
    for uid in uid_dict:
        current_len = len(uid_dict[uid])
        if current_len > most_inquiries:
            most_inquiries = current_len
            longest_session_uid = uid

    return longest_session_uid

    # alternative
    # return max(uid_dict, key=lambda uid: len(uid_dict[uid]))
