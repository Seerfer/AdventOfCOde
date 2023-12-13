while getopts ":y:d:" option; do
  case $option in
    y)
      Year="$OPTARG"
      ;;
    d)
      Day="$OPTARG"
      ;;
    *)
      echo "Allowed flags are y for Year and d for Day"
      exit 1
      ;;
  esac
done

if [ -z "$Day" ] || [ -z "$Year" ]; then
        echo 'Missing -y or -d'
        exit 1
fi

mkdir -p "$Year/Day $Day"

if [ -f "$Year/Day $Day/input" ]; then
  echo "input file exists"
else
  curl -s https://adventofcode.com/$1/day/$2/input >> "$Year/Day $Day/input"

fi


if [ -f "$Year/Day $Day/main.py" ]; then
  echo "main.py file exists"
else
  echo '

    if __name__ == "__main__":
      with open("input", "r") as f:' > "$Year/Day $Day/main.py"

fi


if [ -f "$Year/Day $Day/tests.py" ]; then
  echo "tests.py file exists"
else
  echo 'import unittest


  class Test_Mapper_calculate_range_nums(unittest.TestCase):
    def test_example_test(self):
      self.assertEqual(2+2, 4)' > "$Year/Day $Day/tests.py"
fi

git add "$Year/Day $Day"