def do_connect(SSID, PASSWORD):
    import network
    
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Conectado a la Red")
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)
        while no sta_if.isconnected():
            pass
    print("Configuracion de la Red", sta_if.ifconfig())
    