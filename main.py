import json
import obsws_python as obs

from contextlib import suppress
from dotmap import DotMap
from websockets.sync.client import connect

import config


def main():
    client = obs.ReqClient(host='localhost', port=4455, password=config.OBS_WEBSOCKET_PASSWORD, timeout=3)
    screen = None

    while True:
        try:
            with connect(f'wss://smx.573.no/api/machines/{config.SMX_OCR_IDENTIFIER}') as websocket:
                while True:
                    message = websocket.recv()
                    data = DotMap(json.loads(message))

                    print(f'screen: {data.screen}, visible: {data.visible}')

                    next_scene = None

                    # A screen is visible, use this screen's 'in' scene
                    if data.visible:
                        screen_config = config.SCREENS.get(data.screen, {})
                        next_scene = screen_config.get('in')

                    # Use the previous screen's 'out' scene if the current visible screen doesn't have a scene
                    if data.screen != screen and data.visible and not next_scene:
                        screen_config = config.SCREENS.get(screen, {})
                        next_scene = screen_config.get('out')

                    screen = data.screen

                    if next_scene:
                        scene = next_scene
                        print(f'Switching to {scene}')

                        with suppress(Exception):
                            client.set_current_program_scene(scene)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
