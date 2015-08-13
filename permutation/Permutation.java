class Person{
	private String name;
	
	public Person(String name){
		this.name = name;
	}
	
	public String toString(){
		return this.name;
	}
}
public class Permutation<T> {
	
	private T[] arr;
	
	public Permutation(T[] arr){
		this.arr = arr;
	}
	
	public void swap(int x, int y){
		T tmp = arr[x];
		arr[x] = arr[y];
		arr[y] = tmp;
	}
	
	public void doEach(int s){
		if(s == arr.length){
			print();
		}else{
			for(int i = s; i < arr.length; i++){
				swap(s, i);
				doEach(s+1);
				swap(s, i);
			}
		}
	}
	
	public void permute(){
		doEach(0);
	}
	
	public void print(){
		for(int i = 0; i < arr.length; i++){
			System.out.print(arr[i]);
		}
		
		System.out.println("");
	}

	public static void main(String[] args) {
		Integer[] arr = {1, 2, 3};
		String[] arr1 = {"a", "b", "c"};
		
		Person person1 = new Person("person1");
		Person person2 = new Person("person2");
		Person person3 = new Person("person3");
		
		Person[] persons = { person1, person2, person3 };
		
		Permutation<Integer> p = new Permutation<Integer>(arr);
		Permutation<String> p1 = new Permutation<String>(arr1);
		
		Permutation<Person> p2 = new Permutation<Person>(persons);
		
		p.permute();
		p1.permute();
		p2.permute();
	}

}
