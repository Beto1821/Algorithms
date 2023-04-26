def study_schedule(permanence_period, target_time):
    try:
        count = 0
        for period in permanence_period:
            if period[0] <= target_time and period[1] >= target_time:
                count += 1
        return count
    except Exception:
        return None


""" permanence_periods = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5), ...],
 target_time = 5, expected = 3

     @pytest.mark.parametrize(
         "permanence_periods, target_time, expected",
         [
             ([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5), (6, 7)], 5, 3),
             ([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 1, 2),
             ([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5)], 3, 2),
             ([(1, 1), (2, 2), (3, 3), (4, 4)], 1, 1),
             ([(1, 2), (1, 3), (2, 3)], 2, 3),
         ],
     )"""
