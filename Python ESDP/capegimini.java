Class Capgemini
{
    public static void main(String args[])
    {   
        Capgemini obj = new Capgemini();
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter no of semseter");
        int n = sc.nextInt();
        for(int i=0;i<=n;i++)
        {
            System.out.println("Enter "+n + " th semster subject marks");
            for(int j = 0;j<=i;j++)
            {
                System.out.println("Enter " + n+ " th sub marks: ");
                int marks = sc.nextInt();
                System.out.println("Maximum marks in semster: "Math.max(marks));
            }
        }
    }
        
}