package Q3;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.HashMap;
import java.util.Map;

public class PollutionCheck {
    public static void main(String [] args) throws Exception {
        /*
         * Implement this function to produce the desired outputs
         */
        HashMap<String,Car> Car = new HashMap<>();
        HashMap<String,Truck> Truck = new HashMap<>();
        File file1 = new File("vehicles.txt");
        File file2 = new File("pollution.txt");
        File file3 = new File("queries.txt");
        BufferedReader p1
            = new BufferedReader(new FileReader(file1));
        BufferedReader p2
            = new BufferedReader(new FileReader(file2));
        BufferedReader p3
            = new BufferedReader(new FileReader(file3));   
        String st;
        while ((st = p1.readLine()) != null){
            String d[]=st.split(", ");
            if(d[3].equals("Car")){
                Car c = new Car(d[0], d[1], d[3]);
                Car.put(d[0],c);
            }
            if(d[3].equals("Truck")){
                Truck t = new Truck(d[0], d[1], d[3]);
                Truck.put(d[0],t);
    }
}
        p1.close();
        while ((st = p2.readLine()) != null){
            String d[]=st.split(", ");
            if(Car.containsKey(d[0])){
                Car.get(d[0]).CO2 = Double.parseDouble(d[1]);
                Car.get(d[0]).CO= Double.parseDouble(d[2]);
                Car.get(d[0]).HC = Double.parseDouble(d[3]);
                Car.get(d[0]).checkPollutionStatus();
            }
            else if(Truck.containsKey(d[0])){
                Truck.get(d[0]).CO2 = Double.parseDouble(d[1]);
                Truck.get(d[0]).CO= Double.parseDouble(d[2]);
                Truck.get(d[0]).HC = Double.parseDouble(d[3]);
                Truck.get(d[0]).checkPollutionStatus();
            }
        }
        p2.close();
        while ((st = p3.readLine()) != null){
            String d[]=st.split(", ");
            if(Car.containsKey(d[0])){
                System.out.println(Car.get(d[0]).pollutionStatus);
            }
            else if(Truck.containsKey(d[0])){
                System.out.println(Truck.get(d[0]).pollutionStatus);
            }
            else{
                System.out.println("NOT REGISTERED");
            }
        
    }
    p3.close();
    }
}

