package Java;

import java.util.Scanner;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Random;
import java.io.FileWriter;

public class Raffle {
    public static void main(String[] args) {
        Random rd = new Random();
        Scanner sc = new Scanner(System.in);
        Queue<Toys> qu = new LinkedList<>();
        LinkedList <Toys> result = new LinkedList<>();
        while (true) {
            System.out.print("Выберите действие:\n" + 
                            "* - Добавить новые игрушки на склад\n" +
                            "+ - Машина подберёт случайный приз\n" +
                            "- - Убрать приз из списка невыданных призов\n" +
                            "ex - Закрыть приложение\n");
            String input = sc.nextLine();
            if (input.equals("ex")){
                sc.close();
                break;
            }
            switch (input) {
                case "*":
                    System.out.print("Введите название: ");
                    String name = sc.nextLine();
                    System.out.print("Введите количество: ");
                    String sizeStr = sc.nextLine();
                    while (!sizeStr.matches("\\d+") || Integer.parseInt(sizeStr) < 1) {
                        System.out.println("Некорректный ввод");
                        System.out.print("Введите количество: ");
                        sizeStr = sc.nextLine();
                    }
                    int size = Integer.parseInt(sizeStr);
                    System.out.print("Введите шанс меньше 100: ");
                    String rareStr = sc.nextLine();
                    while (rareStr != "" && !rareStr.matches("\\d+") || Integer.parseInt(rareStr) > 100 || Integer.parseInt(rareStr) < 1) {
                        System.out.println("Некорректный ввод");
                        System.out.print("Введите шанс меньше 100: ");
                        rareStr = sc.nextLine();
                    }
                    int rare = Integer.parseInt(rareStr);
                    System.out.println("Игрушка 3+? (+ или -)");
                    String response = sc.nextLine();
                    result.add(response == "+" ? new Toys3(name, size, rare) : new Toys12(name, size, rare));
                    break;

                case "+":
                    Boolean lose = true;
                    result.sort(null);
                    for (int i = 0; i < result.size(); i++) {
                        int chance = rd.nextInt(101);
                        if (chance <= result.get(i).getChanse()){
                            qu.add(result.get(i));
                            lose = false;
                            System.out.println(String.format("Победа! Можете получить %s", result.get(i).getName()));
// Удаление игрушки из общего числа производится тут потому-что нечесетно обещать кому-то игрушку, а потом понять что они закончились
                            result.get(i).reduction(); 
                            if (result.get(i).getSize() < 1){
                                result.remove(i);
                            }
                            break;
                        }
                    }
                    if (lose){
                        System.out.println("Поражение");
                    }
                    break;

                case "-":
                    try {
                        if(qu.size() > 0){
                            FileWriter fw = new FileWriter("Игрушки выданы.txt", true);
                            Toys a = qu.remove();
                            fw.write(String.format("Выдана игрушка %s, незарезервированных осталось %d\n", a.getName(), a.getSize()));
                            fw.close();
                            System.out.println(String.format("Игрушка %s выдана", a.getName()));
                        }
                        else System.out.println("Игрушек на выдачу нет");
                    } catch (Exception e) {
                        System.out.println(e.getMessage());
                    }
                    break;
        
                default:
                    System.out.println("Ошибка ввода");
                    break;
            }
        }
    }
}
