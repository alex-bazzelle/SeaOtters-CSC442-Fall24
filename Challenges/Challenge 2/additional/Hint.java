import java.lang.reflect.*;

class Hint {
    private int length = 20000;

    public Hint() {
    }

    public int getLength() {
        return this.length;
    }

    public void setLength(int var1) {
        if (var1 > 0) {
            this.length = var1;
        }

    }

    private void superprivatefunction() {
        String var1 = "68696e743a20596f752061726520736f20636c6f73652e20596f752073686f756c6420686176652072656365697665642061207368613235362068617368206f66207468652066696e616c2070617373776f726420796f75276c6c206e65656420746f206f70656e20746865207064662e205468652061637475616c2070617373776f72642069732061637475616c6c79206120636f6e636174656e6174696f6e206f662074776f206f662074686520746f70203130302070617373776f726473206f6620323032322073657061726174656420627920612032206469676974206e756d6265722e20416e206578616d706c65206f66207375636820612070617373776f726420776f756c642062652070617373776f726430357177657274792041206c6973742063616e20626520666f756e642061743a2068747470733a2f2f74696e7975726c2e636f6d2f656535386261637020596f752073686f756c642062652061626c6520746f207772697465206120717569636b2073637269707420746f206861736820616c6c20706f737369626c6520636f6d62696e6174696f6e73206f662074686f73652070617373776f72647320616e642064696769747320616e6420636f6d7061726520697420746f207468652070726f7669646564206861736820696e206f7264657220746f2066696e642074686520636f72726563742066696e616c2070617373776f726420746f20756e6c6f636b2074686520706466";
        StringBuilder var2 = new StringBuilder();
        int var3 = this.length * 2;
        int var4 = Math.min(var3, var1.length());

        for (int var5 = 0; var5 < var4; var5 += 2) {
            String var6 = var1.substring(var5, var5 + 2);
            var2.append((char) Integer.parseInt(var6, 16));
        }

        System.out.println(var2);
    }
    public static void main(String[] args) throws NoSuchMethodException, InvocationTargetException, IllegalAccessException {
        Hint t = new Hint();
        Class c = t.getClass();
        try {
            Constructor con = c.getConstructor();
            System.out.println("The name of the class is " + c.getName());
            System.out.println("Its constructor is " + con.getName());
        } catch (Exception e) {
        }
        System.out.println("-----------------------------");
        Method[] methods = c.getMethods();
        for (Method m : methods) {
            System.out.println(m.getName());
        }
        System.out.println("-----------------------------");
        Method[] allMethods = c.getDeclaredMethods();
        for (Method m : allMethods) {
            System.out.println(m.getName());
        }
        System.out.println("-----------------------------");
        Method methodcall1 = c.getDeclaredMethod("superprivatefunction");
        methodcall1.setAccessible(true);
        methodcall1.invoke(t);
    }
}
