# Random String Generator

This Python script generates a random string of specified length and copies it to the clipboard using the `pyperclip` module.

## Usage

To generate a random string, call the `generate_random_string` function and provide the desired length as an argument. The generated string will be copied to the clipboard and returned by the function.

```python
random_string = generate_random_string(length)
```

Replace `length` with the desired length of the random string.

## Example

Here's an example usage of the script:

```python
random_string = generate_random_string(12)

print("This is your random password:")
print(random_string)
```

Running the script will generate a random password of length 12 and display it in the console.

## Dependencies

This script requires the `random` and `pyperclip` modules. If you don't have them installed, you can install them using `pip`:

```bash
pip install random pyperclip
```

Note: `pyperclip` module may require additional setup on some systems. Please refer to the module's documentation for instructions.

## License

This code is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and use it in your own projects.
