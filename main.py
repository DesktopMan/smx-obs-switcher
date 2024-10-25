import json
import obsws_python as obs

from dotmap import DotMap
from websockets.sync.client import connect

import config


def main():
    client = obs.ReqClient(host='localhost', port=4455, password=config.OBS_PASSWORD, timeout=3)

    while True:
        try:
            with connect(f'wss://smx.573.no/api/machines/{config.SMX_OCR_MACHINE}') as websocket:
                while True:
                    message = websocket.recv()
                    data = DotMap(json.loads(message))

                    print(f'screen: {data.screen}, visible: {data.visible}')

                    screen_config = config.SCREENS.get(data.screen, {})
                    scene = screen_config.get('in') if data.visible else screen_config.get('out')

                    if scene:
                        print(f'Switching to {scene}')
                        client.set_current_program_scene(scene)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
