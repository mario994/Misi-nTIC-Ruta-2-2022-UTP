public class PrecioTotal {
    private double totalDispositivos;
    private double totalPortatiles;
    private double totalTablets;
    private Dispositivo [] listaDispositivos;

    PrecioTotal(Dispositivo[] pDispositivos) {

    }

    public void mostrarTotales() {
        System.out.println("Totalización precios computadores portátiles " + totalPortatiles);
        System.out.println("Totalización precios tabletas " + totalTablets);
        System.out.println("Totalización precios dispositivos " + totalDispositivos);
        }
    }
    





class Dispositivo {
    protected final int PESO_BASE = 1;
    protected final char CONSUMO_W_BASE = 'F';
    protected final double PRECIO_BASE = 100.0;

    protected int peso;
    protected char consumoW;
    protected double precioBase;

    public Dispositivo() {
        peso = PESO_BASE;
        consumoW = CONSUMO_W_BASE;
        precioBase = PRECIO_BASE;
    }

    public Dispositivo(Double precioBase, Integer peso) {
        this.precioBase = precioBase;
        this.peso = peso;
        consumoW = CONSUMO_W_BASE;
    }

    public Dispositivo(Double precioBase, Integer peso, char consumoW) {
        this.precioBase = precioBase;
        this.peso = peso;
        this.consumoW = consumoW;
        calcularConsumoW();
    }
        
    public void calcularConsumoW(){
        if(){
                this.consumoW=consumoW;
            } else {
    
            }
    }
        public Double calcularPrecio(){
            // return precioBase + adicion;
        }
    }
    
class Tablet extends Dispositivo {
    protected final int MEMORIA_RAM_BASE = 1;
    protected int memoriaRam;

    public Tablet() {
        this.precioBase = PRECIO_BASE;
        this.peso = PESO_BASE;
        this.consumoW = CONSUMO_W_BASE;
        this.memoriaRam = MEMORIA_RAM_BASE;
    }
        
    public Tablet(Double precioBase, Integer peso) {
        this.precioBase = precioBase;
        this.peso = peso;
        this.consumoW = CONSUMO_W_BASE;
        this.memoriaRam = MEMORIA_RAM_BASE;
    }
        
    public Tablet(Double precioBase, Integer peso, char consumoW, Integer memoriaRam) {
        this.precioBase = precioBase;
        this.peso = peso;
        this.consumoW = consumoW;
        this.memoriaRam = memoriaRam;
    }
        
    public Double calcularPrecio() {
        int adicion = 0;

        if(this.memoriaRam > 1 && this.memoriaRam <= 2){
            adicion += 5;
        } else if (this.memoriaRam > 2 && this.memoriaRam <= 4) {
            adicion += 25;
        } else {
            adicion += 50;
        }
    }
    }
    
    class Portatil extends Dispositivo {
        public Portatil() {

        }
        
        public Portatil(Double precioBase, Integer peso) {

        }
        
        public Portatil(Double precioBase, Integer peso, char consumoW, Integer discoDuro) {

        }
        
        public Double calcularPrecio() {

        }
    }


public class App {
    
    public static void main(String[] args) {
        
    }
}
