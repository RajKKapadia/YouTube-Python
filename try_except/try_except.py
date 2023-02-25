try:
    print(2 / 0)
except Exception as e:
    print(e)
else:
    print('Code ran successfully.')
finally:
    print('Always run.')