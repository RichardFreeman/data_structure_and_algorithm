
public class TrainSchedule {
	
	public static int getTrains(int count){
		
		if(count < 2){
			return 1;
		}else{
			int result = 0;
			for(int i = 0; i < count; i++){
				result = result + getTrains(i) * getTrains(count-i-1);
			}
			return result;
		}
	}

	public static void main(String[] args) {
		int count = TrainSchedule.getTrains(3);

		System.out.println(count);
	}

}
