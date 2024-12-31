from pynput import keyboard
import logger

# The event listener will be running in this block
with keyboard.Events() as events:
    for event in events:
        if event.key == keyboard.Key.esc:
            print('Exiting program...')
            break
        else:
            print('Received event {}'.format(event))
            logger.log(event)
