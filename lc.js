function increment(nums) {
  temp = 0;
  len = nums.length;
  for (let i = 0; i < len; i++) {
    if (nums[i] > temp) {
      temp = nums[i];
      index = i;
    }
    temp = temp + 1;
    nums[index] = temp;
  }
  return nums;
}
increment([1, 5, 4]);
console.log(increment());
