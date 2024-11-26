def do_connect(SSID,PASSWORD):
    import network
    
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("conectado a la red")
        sta_if.active(True)
        sta_if.connect(SSID,PASSWORD)
        while not sta_if.isconnected():
            pass
    print("CONFIGURACION",sta_if.ifconfig())