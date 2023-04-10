package Java;


public abstract class Toys implements Comparable<Toys>{
    private static int id = 1;
    private int toyID = id;
    private String name;
    private int quantity;
    private int rarity;

    
    public Toys(String name, int size, int rare) {
        this.name = name;
        this.quantity = size;
        this.rarity = rare;
        id++;
    }


    public int getChanse(){
        return this.rarity;
    }


    public int getSize(){
        return this.quantity;
    }


    public String getName(){
        return this.name;
    }


    public void changeRarity(int a) {
        if (a < 101){
            rarity = a;
        }
        else{
            System.out.println("Ошибка: больше 100%");
        }
    }


    public void reduction() {
        this.quantity--;
    }


    @Override
    public int compareTo(Toys other) {
        if (this.rarity < other.rarity) {
            return -1;
        } else if (this.rarity > other.rarity) {
            return 1;
        } else {
            return 0;
        }
    }
}
