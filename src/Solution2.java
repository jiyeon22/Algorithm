//2022_1018_
//프로그래머스 lv1 k번째 수 
import java.util.ArrayList;
import java.util.Arrays;

public class Solution2 {
	public static int[] solution(int[] array, int[][] commands) {
		
		int answer[] = new int[commands.length];
		
		
		
		
		for(int a = 0; a < commands.length; a++) {
				int i = commands[a][0];
				int j = commands[a][1];
				int k = commands[a][2];
				System.out.println("i,j,k: "+ i+ j+ k);
				int [] temp = new int[j-i+1];
				for(int b = 0; b < temp.length; b++) {
					temp[b] = array[b+i-1];
					System.out.println("temp값 "+ Arrays.toString(temp));
				}
				Arrays.sort(temp);
				answer[a] = temp[k-1];
				
				
			}
			
		
		
		
		return answer;
	}
	
	public static void main(String[] args) {
		int[] array = {1,5,2,6,3,7,4};
		int[][] commands = {{2,5,3},{4,4,1},{1,7,3}};
		System.out.println(Arrays.toString(solution(array, commands)));
	}
	
	

}


//다른 사람의 풀이 
/*
class Solution1{
	public int[] solution(int[] array, int[][] commands) {
		int [] answer = new int[commands.length];
		
		for(int i = 0; i < commands.length; i++) {
			int[] temp = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);
			Arrays.sort(temp);
			answer[i] = temp[commands[i][2]-1];
		}
		return answer;
	}
}
*/
//copyOfRange!!!!!!!!!!
