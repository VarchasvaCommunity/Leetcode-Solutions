class Solution {
    public int firstMissingPositive(int[] nums) {
        int i=0;
        while(i<nums.length){
            int correct=nums[i]-1;
            if(nums[i]<nums.length&&nums[i]>0 && nums[i]!=nums[correct]){
                swap(nums,i,correct);
            }else{
                i++;
            }
        }
        int counter=0;
        
        for(int j=0;j<nums.length;j++){
            if(nums[j]!=j+1){
                return j+1;
            }else{
                counter++;
            }  
    
        }

        if(counter==nums.length)
            return counter+1;

        return -1;
    }

    public void swap(int[] arr, int a, int b){
        int temp=arr[a];
        arr[a]=arr[b];
        arr[b]=temp;
    }
}
