import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.Iterator;
import java.util.ListIterator;
//프로그래머스 lv1 두 개 뽑아서 더하기
/*
 //*2022_1018
 * 정수 배열 numbers가 주어집니다. 
 * numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 
 * 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.


알아야될 개념
1)ArrayList 
-ArrayList<Integer> arr1 = new ArrayList<Integer>(); // 타입지정
-ArrayList<Integer> arr2 = new ArrayList<>(); 타입 생략 가능
-ArrayList<Integer> arr3 = new ArrayList<>(10); 초기용량설정
-ArrayList<Integer> arr4 = new ArrayList<>(arr1); 다른 collection값으로 초기화
생성할때 Set이나 다른 ArrayList를 전달하면 해당 Collection 값으로 초기화 

-ArrayList<Integer> arr5 = new ArrayList<>(Arrays.asList(1,2,3,4,5));
 가변 인자를 전달받는 Arrays.asList() 
 
add() - 엘레멘트 추가 / 리스트의 가장 끝에 값을 추가 
set() 기존에 추가된 값 면경 ex) arr.set(0, "12");
remove() 삭제 -인덱스 입력 또는 엘레멘트 입력 
claer() 내용 전체 삭제 
 */
/*class Solution {
	
	public static void main(String[] args) {
		ArrayList<Integer> arr1 = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
		
		Iterator iterator = arr1.iterator();
		while(iterator.hasNext()) {
			System.out.println(iterator.next()+" ");
		}
		System.out.println();
		
		System.out.println(arr1.contains(2));
		System.out.println(arr1.indexOf(7));

		Integer [] arr2 = {1, 24, 30, 5, 99};
		Arrays.sort(arr2);
		System.out.println(Arrays.toString(arr2));
		
		//collections Integer[]로 변수 선언 
		Arrays.sort(arr2, Collections.reverseOrder());
		System.out.println(Arrays.toString(arr2));
		
	}

}*/

class Solution{
	public static int[] solution(int[] numbers) {
		ArrayList<Integer> arr = new ArrayList<>();
		
		int sum;
		for(int i = 0; i < numbers.length-1; i++) {
			for(int j = i+1; j < numbers.length; j++) {
				sum = numbers[i] + numbers[j];
				System.out.println("sum값:"+sum);
				if(arr.indexOf(sum) < 0) {
				arr.add(i, sum); 
				}
			}
				
		}
		
		int [] answer = new int[arr.size()];
		for(int i =0; i < answer.length; i++) {
			answer[i] = arr.get(i);
		}
		Arrays.sort(answer);
		
		return answer;
	}
	
	public static  void main(String[] args) {
		int [] num = {5,0,2,7};
		System.out.println(Arrays.toString(solution(num)));
		
	}
}
