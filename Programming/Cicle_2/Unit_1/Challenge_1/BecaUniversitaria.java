public class BecaUniversitaria {
    public int pTiempo;
    public double pMonto; 
    public double pInteres;
    
    public BecaUniversitaria() {
        this.pTiempo = 0;
        this.pMonto = 0;
        this.pInteres = 0;
    }

    public BecaUniversitaria(int pTiempo, double pMonto, double pInteres){
        this.pTiempo = pTiempo;
        this.pMonto = pMonto;
        this.pInteres = pInteres;
    }

    public double calcularInteresSimple(){
        double interesSimple = this.pMonto * (this.pInteres /100) * this.pTiempo;
        return Math.round(interesSimple);
    }
    
    public double calcularInteresCompuesto(){
        double interesCompuesto = this.pMonto * (Math.pow(1 + (this.pInteres / 100), this.pTiempo) - 1);
        return Math.round(interesCompuesto);
    }

    public String compararInversion (int pTiempo, double pMonto, double
pInteres){
        this.pTiempo = pTiempo;
        this.pMonto = pMonto;
        this.pInteres = pInteres;
        double diferencia = calcularInteresCompuesto() - calcularInteresSimple();
        return "La diferencia entre la proyección de interés compuesto e interés simple es: $" + diferencia; 
    }
    
    public String compararInversion(){
        double diferencia = calcularInteresCompuesto() - calcularInteresSimple();
        if(diferencia == 0){
            return "No se obtuvo diferencia entre las proyecciones, revisar los parámetros de entrada.";
        } else {
            return "La diferencia entre la proyección de interés compuesto e interés simple es: $" + diferencia; 
        }
    }

    public static void main(String[] args) {
        BecaUniversitaria beca1 = new BecaUniversitaria(48, 10000, 2.0);
        // BecaUniversitaria beca2 = new BecaUniversitaria(48, 10000, 2.0);
        // BecaUniversitaria beca3 = new BecaUniversitaria();

        // System.out.println(beca1.compararInversion());
        // System.out.println(beca1.calcularInteresCompuesto());
        // System.out.println(beca1.calcularInteresSimple());
        // System.out.println(beca1.compararInversion());
        // System.out.println(beca2.compararInversion());
        // System.out.println(beca3.compararInversion());
        // System.out.println(beca1.compararInversion(60, 13000, 1.4));
        System.out.println(beca1.calcularInteresCompuesto());
        System.out.println(beca1.calcularInteresSimple());
        System.out.println(beca1.compararInversion(48, 10000, 2.0));
        // System.out.println(beca1.compararInversion());

    }
}
