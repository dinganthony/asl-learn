import mediapipe as mp

def distance(l1, l2):
    return (l1[0] - l2[0]) * (l1[0] - l2[0]) +
     (l1[1] - l2[1]) * (l1[1] - l2[1]) +
      (l1[2] - l2[2]) * (l1[2] - l2[2])

def compute_distances(landmarks):
    num_landmarks = len(landmarks)
    if not landmarks or num_landmarks <= 0:
        return []
    average = [0, 0, 0]
    for i in range(num_landmarks):
        average[0] = average[0] + landmarks.landmark[i].x
        average[1] = average[1] + landmarks.landmark[i].y
        average[2] = average[2] + landmarks.landmark[i].z
    average[0] = average[0] / num_landmarks
    average[1] = average[1] / num_landmarks
    average[2] = average[2] / num_landmarks

    landmark_list = []
    for i in range(num_landmarks):
        landmark = landmarks.landmark[i]
        landmark_list.append([landmark.x - average[0], landmark.y - average[1], landmark.z - average[2]])

    distances = [[] for i in range(num_landmarks)]
    for i in range(num_landmarks):
        for j in range(num_landmarks):
            distances[i].append(distance(landmark_list[i], landmark_list[j]))
    return distances  

def distance_diff(curr, test):
    diff = 0
    assert len(curr) > 0
    assert len(curr) == len(test)
    for i in range(len(curr)):
        for j in range(len(curr[0])):
            diff += abs(curr[i][j] - test[i][j])

def find_best_letter(current, answers):
    distances = compute_distances(current)
    min_diff = float('inf')
    best_ans = 0
    for i in range(len(answers)):
        diff = distance_diff(distances, compute_distances(answers[i]))
        if diff < min_diff:
            min_diff = diff
            best_ans = i
    return 'A' + best_ans