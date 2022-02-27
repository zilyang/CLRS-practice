class InsertionSort {
    public int[] sortArray(int[] input) {

        if (input.length < 2) {
            return input;
        }

        for (int i = 1; i < input.length; i++) {
            int key = input[i];
            int j = i - 1;
            while (j >= 0 && input[j] > key) {
                input[j + 1] = input[j];
                j--;
            }
            input[j + 1] = key;
        }

        return input;

    }
}
