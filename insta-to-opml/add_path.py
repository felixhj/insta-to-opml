import os

# Determine the current shell type
shell_type = os.environ['SHELL']

# Determine the shell configuration file based on the shell type
if 'bash' in shell_type:
    config_file = os.path.expanduser('~/.bash_profile')
elif 'zsh' in shell_type:
    config_file = os.path.expanduser('~/.zshrc')
else:
    print("Unsupported shell type:", shell_type)
    exit(1)

# Append the export statements to the shell configuration file
with open(config_file, 'a') as f:
    f.write('\nexport PATH="/usr/local/bin:/usr/local/bin/pip:$PATH"\n')

# Reload the shell configuration
os.system(f'source {config_file}')
