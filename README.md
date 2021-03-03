# Keylogger

Keylogger is a Python script which captures every keystroke. It logs in such a format so that it is easy to analyze and read from the log file.


## Description

```python
• Used Python Language to build Keylogger.

• Used a listener function that listens to every key that is pressed
and calls the function add_key.

• add_key function pushes the key entered in an array. If entered key
is Enter, the text gets added in the log file with the help of function
write_file.

• In write_file function:
➢ log.txt is first opened in which text will be added.
➢ The current timestamp is calculated using datetime.now()
➢ For every key present in the array, if the key is of special
type (eg. Enter, Tab, Space, etc.), then ‘<>’ is added to
indicate them in log file clearly, else key is added to the log file
as it is.
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
