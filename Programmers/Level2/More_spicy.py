import heapq


def solution(scoville, K):

	# 기존 리스트를 힙으로 변환
	heapq.heapify(scoville)

	mix_count = 0

	while scoville[0] < K:

		if len(scoville) == 1:
			return -1

		# 가장 맵지 않은 음식의 스코빌 지수와, 두 번째로 맵지 않은 스코빌 지수 꺼냄
		lowest_scoville = heapq.heappop(scoville)
		second_lowest_scoville = heapq.heappop(scoville)

		# 섞은 음식의 스코빌 지수 생성
		new_scoville = lowest_scoville + (second_lowest_scoville * 2)

		# 섞은 개수 1 증가
		mix_count += 1

		# 섞은 음식의 새로운 스코빌 지수 추가
		heapq.heappush(scoville, new_scoville)

	return mix_count