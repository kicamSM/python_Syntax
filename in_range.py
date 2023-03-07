def in_range(nums, lowest, highest):
  
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits i.e. 20 is greater than the lowest number 15 
      30 fits i.e. 30 is equal to the highest number 
    """
    my_list = []
    for num in nums:
      if num >= lowest and num <= highest:
        print(f"{num} fits")


in_range([10, 20, 30, 40, 50], 15, 30)            
