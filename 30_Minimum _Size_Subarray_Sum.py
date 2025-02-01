def minSubArrayLen(target, nums):
    left = 0
    current_sum = 0
    min_length = float('inf')  # Valor muy grande

    for right in range(len(nums)):
        current_sum += nums[right]  # Expandir la ventana

        while current_sum >= target:  # Reducir la ventana si se cumple la condición
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1  # Mueve el puntero izquierdo para minimizar la ventana

    return min_length if min_length != float('inf') else 0
