import java.util.*;

class QuickSort{

	private static int counter = 0;

    /** 
     * @param list
     */
    private static <Object extends Comparable<Object>> void quickSort(List<Object[]> list){
        sort(list,0,list.size()-1);
    }
    
    /** 
     * @param list
     * @param first
     * @param last
     */
    private static <Object extends Comparable<Object>> void sort(List<Object[]> list,int first,int last){
        if(first < last){
            int pivIndex = partition(list, first, last);
            sort(list,first,pivIndex - 1);
            sort(list,pivIndex + 1,last);
        }
    }

    
    /** 
     * @param list
     * @param first
     * @param last
     * @return int
     */
    private static <Object extends Comparable<Object>> int partition(List<Object[]> list, int first,int last){

        Object pivot = list.get(first)[0];
        int left = first,
            right = last;

        do{
            
            while( (left < last) && (pivot.compareTo(list.get(left)[0]) >= 0) )
                left++;

            while(pivot.compareTo(list.get(right)[0]) < 0)
                right--;

            if(left < right){
                swap(list,left,right);
            }
        }while(left < right);

        swap(list,first,right);
        return right;

    }

    /** 
     * @param list
     * @param left
     * @param right
     */
    private static <Object extends Comparable<Object>> void swap(List<Object[]> list,int left, int right){

        Object[] tmp = list.get(left);
        list.set(left, list.get(right));
        list.set(right, tmp);
        counter++;
    }
	public static void main(String[] args){

		ArrayList<Integer[]> ll = new ArrayList<Integer[]>();
		Integer[] arr0 = new Integer[1];
		Integer[] arr1 = new Integer[1];
		Integer[] arr2 = new Integer[1];
		Integer[] arr3 = new Integer[1];
		Integer[] arr4 = new Integer[1];
		Integer[] arr5 = new Integer[1];
		Integer[] arr6 = new Integer[1];
		Integer[] arr7 = new Integer[1];


		// arr0[0] = 8;
		// arr1[0] = 6;
		// arr2[0] = 4;
		// arr3[0] = 2;
		// arr4[0] = 1;
		// arr5[0] = 3;
		// arr6[0] = 5;
		// arr7[0] = 7;

		// arr0[0] = 8;
		// arr1[0] = 7;
		// arr2[0] = 6;
		// arr3[0] = 5;
		// arr4[0] = 4;
		// arr5[0] = 3;
		// arr6[0] = 2;
		// arr7[0] = 1;

		arr0[0] = 1;
		arr1[0] = 2;
		arr2[0] = 3;
		arr3[0] = 4;
		arr4[0] = 5;
		arr5[0] = 6;
		arr6[0] = 7;
		arr7[0] = 8;


		ll.add(arr0);
		ll.add(arr1);
		ll.add(arr2);
		ll.add(arr3);
		ll.add(arr4);
		ll.add(arr5);
		ll.add(arr6);
		ll.add(arr7);


		quickSort(ll);

		System.out.println(counter);

	}
}