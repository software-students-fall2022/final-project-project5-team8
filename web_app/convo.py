from pyChatGPT import ChatGPT
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def convo(sent, valid, inp):
    
    session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..M8lcKu_EG0VwPAnY.sXLal7IF35a2iQZTDx7-RAM4j7Pevn8rf0D8e0IPPKG7-EF5TF2_vvnDeIarpSaXHlJeozGK_QxLvW5Uc1pKzF3LB72n7ndrIbXo2AQAlFFvrn7qydyv6xvWxo3pnkEnfdwMWrn3RJYbUMY0980GKQt3ZUQXKdPcQG5qtUZaxg0PO4HM120SdSfekTSVilfOemfB_uudLO6mzAv6JnXR5aSZYCb0Vz8NIZzm5Og0tDHKxyAufHLZq0T_ebpMveEpTQazBwIjYVAu_YELZ7Hqt-sOlrweaTvf1PBfmQh9FAU9KF1uz0gEC7MOQ6gm4jFq3X1w_fhC8Df4Bee3YWoxhiG_sNrloiYopO2TpDJdzdlxj4awaiVsKD2JUoDuhdOWhJmSdOz_g2xVEDWW_eCu27Kek2jyVJcNzIVWlpSe-74N6AwuHIt__g-Y3FpmTkDGZMlEsTlJUi1XPbsFuU4DVmh2ZgP-_Gny7emlpb2FkPU0Xb3UJuTs3HqcK7AvJjTApsinJFZSnfu6mtJLYGyEBJITMVnE1sylvbA63J6N7wITJjlVtF-sOAc2p1R9KoMTprJmSR2yzUo5fIJOVm7K-WhGIyk1g6FHKCJ1_VXxEUJE3u8GD9lkB89RACiVrZhqsCdqmzGs0CghGWc2Bv4ivC3I2eZgORc9C8GvCn_VBm33YCY9FvUb4TY5Zvc3_5i-n304kK6AZ295i4VQkRPjx6CjS5-1vA75CsTTfq-qeNIORnh-VNd7FZ6yqsv6SW3H1or4cLo6z1W4Tlh3RQgFs6CmmOHnymQ9RqPDqyCYkkbRZdoHrhCgdO9qjzIaPwIei42QIJLZtBrBwrCdCbkXMA6L8fFyyAHYA8uvdr90jkxIZALDrKZKR1GDwe5l1sEjLP1QunWsx9MV4HhQYTuiZlfGjeWfIKSLzleWzs8lhLKFbbNGoW5H1EAsbJmoJh7HondIxtROUFh_F5xw-3PFR23NJNGlzCVPIWEay8DSvbc4CUonYOG3Cf3hVV83zwcAB0OCcw0undx2cuxq5GaZYYCWodQCTG8slqBUB59--cNi8FkZsD_wbSftnRdOIoQqHpIzAFhk6rv9bsYNHNC9ghHgdGzCCTWwEH0K90s7ojOVKmFmZ2IFPVXTlTu9sa5t4aSd7C7AC9UzgQm3IqD0SO1GSWM9qd-f9706BrsbjYdHjRisc4oILpozsMykZLZ6t07Z4EM-QIdXZUB6vkfud3KwSx-NVeHmvlydkm1sBppI-W3tYqZHC4PNfpA327u7U6qhyXGcZFplclYhSvAyHP3C1YYbjzDG-W6YHVGfSSGFh0vyTtrOYJuM-YxmgOGeyUP-8loQ_f_EK-bd7Eud7Wd3IhceolfZuxS9-alvnKQ_BOF-xRHyPGjEsmI33Nz53ty-q-iB-Vkdf5b4Nddc3pDUq6dIzsELEvxfE5BtugD7_PuBqm-yPMV2YW6E6RM1xN7OF057_1IPOAEzN68OMZl5rBqD1OiE98YAnPRA2W68BY4cshweXGrjaz-TnBbFHrfKVUm3Yj-FvbsXF0ap1LAl50JY75noYLgKTEBq1txopp1YOZThCVzY034YgwFg46INqEhLbsEWC0dZau_2HNodoAd_798eugEDcSIm3yi0c3X1HTYm520_3xUgK5Rg6ZJVna8iimePfiDmtE9qj54mUQlgIslgcGzvOuvlcFczaoXg7nbwD-VLOzpYZXf12P5eTa8A_SCW2DuTd5E1BglWUk2TaIzaQoVzsQWYQQF3VWDXHPdvkxrq6lAGNtj9tL6eDK9O059_sf8n3AExUc1fIQS7AooGk_kVf3SyhqV3RmMSIgWYX4QNbOMgKr5CRnrxrkREcl2bBPeapR-QabKpHbC5qqMW1jcGbHYZTkV1SdKk8_CmCV3cFI5GwcCeIm1bEjRzPptltXIUuiC-pG85crqegzHYBcbsLrrRkC5-t0PhorMy-CNW5W2aGMWmpb1JdYaCOvcRn1pBcALIx7l8pwfRexD3nrr6xVoSQmdZrn3GBi9Immqai0msMXQSVCIzYxgMNvWdkx-A5vasKOHHNtNXvc1qScpUDRNAKFfpSnh6fiV9Ml-QnIhRst4SCMT6V-9v6_GUqooq9ZkbUnk0OmYohmfHyIju46RxRsfkWS_MhiTMCb2hyiWDEqQmdR_EVylg47E28P96EdV5-IBoP6URqehnsHQaYVOBIH75-mbxSKmFcq9S0trCPKpYOrkDpHU2YmUxoWWerHKaWEescM-meXXs0LsYTldQqLKQ8lCgbqCEap-h1bIFAyJENQOj6vJfWBdjYPrdLZyO.8r2wd6nWqBwadcxwHLlzGg'  # `__Secure-next-auth.session-token` cookie from https://chat.openai.com/chat
    api = ChatGPT(session_token)  # auth with session token

    #check to see if user wants to continue convo
    if not valid:
        api.close()  # close the session
    #api2 = ChatGPT(session_token, proxy='http://proxy.example.com:8080')  # specify proxy
    #api3 = ChatGPT(auth_type='google', email='example@gmail.com', password='password') # auth with google login
    #api4 = ChatGPT(session_token, verbose=True)  # verbose mode (print debug messages)
    resp = api.send_message("""I want you to act as a """ + inp +""" translator, spelling corrector and improver. 
    I will speak to you in any language and you will detect the language, translate it and answer in 
    the corrected and improved version of my text, in """+ inp +""". I want you to replace my simplified 
    A0-level words and sentences with more beautiful and elegant, upper level """ + inp+""" words and sentences. 
    Keep the meaning same, but make them more literary. I want you to only reply the correction, 
    the improvements and nothing else, do not write explanations. My first sentence
     is: """+ sent)
    
    #print(resp['message'])
    #api.close()  # close the session
    #api.reset_conversation() # reset the conversation
    api.refresh_auth()
    return resp['message']  

convo("hola como estan", True, "English")