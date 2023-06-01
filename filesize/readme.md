# Folder Size Analyzer

This Python script analyzes the sizes of folders in the root directory of your system using the `du` command. It provides a ranked list of the largest folders along with their sizes.

## Prerequisites

Before using this script, make sure you have the following requirements:

- Python 3.x
- The `tabulate` library (install using `pip install tabulate`)

## Usage

To analyze the sizes of folders in the root directory, run the script with the following command:

```bash
python folder_size_analyzer.py
```

The script will display a table with the top 10 largest folders and their sizes.

## Example Output

Here's an example output of running the script:

```
╒═══════════╤══════════════════════════════════════════════════════════╕
│   Size    │                           Folder                           │
╞═══════════╪══════════════════════════════════════════════════════════╡
│   4.3G    │                           /home                            │
├───────────┼────────────────────────────────────────────────────────────┤
│   1.2G    │                          /var/lib                          │
├───────────┼────────────────────────────────────────────────────────────┤
│   942M    │                          /usr/lib                          │
├───────────┼────────────────────────────────────────────────────────────┤
│   860M    │                          /usr/src                          │
├───────────┼────────────────────────────────────────────────────────────┤
│   756M    │                          /usr/share                        │
├───────────┼────────────────────────────────────────────────────────────┤
│   496M    │                          /var/cache                        │
├───────────┼────────────────────────────────────────────────────────────┤
│   411M    │                           /opt                             │
├───────────┼────────────────────────────────────────────────────────────┤
│   398M    │                          /usr/lib32                        │
├───────────┼────────────────────────────────────────────────────────────┤
│   366M    │                          /usr/bin                          │
├───────────┼────────────────────────────────────────────────────────────┤
│   340M    │                         /usr/local                         │
╘═══════════╧══════════════════════════════════════════════════════════╛
```

## License

This code is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and use it in your own projects.
