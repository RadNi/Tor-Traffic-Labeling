import pyshark


class Cell:
    @staticmethod
    def parse_from_file(file_name):
        cells = []
        f = open(file_name, 'r')
        # f.read()
        labled_arr = f.read().split('------------')
        for l in labled_arr:


            tmp_lines = l.split('\n')
            try:
                application_name = tmp_lines[1].split(' ')[-1]
                decrypted_payload = tmp_lines[2].split(' ')
                payload = tmp_lines[5].split(' ')
                cells.append(Cell(application_name, payload, decrypted_payload))
                # print(application_name, ' ', payload)
                # print(application_name, ' ', tmp_lines[2])

                # if '50 89 33 6a 43 c8 e3 11 61 de 2b 60 71 c4 37 20 7c 0d 8a f5 95 ad 49 0c ee e5 42 61 5d 1a 75 04 8b a1 a4 b8 2d b4 c0 43 48 f2 ba 20 dd 8c 36 5f d6 e7 a1 65 0c 53 20 e8 6b 5a 18 5b 5e a7 cb 3b ed 44 2b 6d 20 86 ee f3 ba 34 a6 61 03 20 1f 58 c6 c8 6a bb 7f 95 90 73 3d 7d 9e 59 51 59 46 2f d1 0b 51 91 2e 6a c0 16 79 e9 56 d1 a7 e8 b5 6a 8a 35 a1 66 a3 0b 9e 75 99 e3 07 25 ad 0d 8f 7d 94 18 b5 54 c8 88 b2 12 4a 34 71 c5 4b 6e 00 b5 0f 16 8c e3 ed f4 7c 3b 29 2f 20 83 ca 27 e7 45 7d b1 5d 66 73 6e ee b7 19 61 cc 95 85 8f c2 8a 60 35 0c e6 ae f9 2e c4 6d 5a f5 e4 f1 80 d8 7b d7 83 2c 3c d5 31 c6 34 e2 d3 88 0a b2 1b 0f cc fd 0a bc ce dc 44 31 27 3f 29 2d 24 ec a7 d9 e0 e3 8e 7d 3d 85 5b ec 96 e1 dd d6 29 c9 dd da e8 cc c7 e7 5e 2d 31 a2 a2 ac b1 66 3a 7c 29 1c 8d 45 c5 da c4 25 d6 68 9c 0e 52 c5 72 e5 df 22 b4 e2 f6 af 9b d3 a7 76 84 05 87 8e 96 66 7b 96 c1 be 37 cf f7 3c 4d df 0f 5b 92 48 6f fc 81 bb b9 d8 ee a7 ac 93 cb 23 51 f8 6c b6 8e 6c 8e c5 a2 7f b9 c2 a7 8e aa f4 21 48 90 3a f1 b3 02 0b ca 5b a9 a0 82 eb cb 75 a7 0b e5 02 18 7b 01 64 c7 32 11 55 89 fe c4 21 8f 42 f7 5c df 43 5a 79 bc 96 5c 2a 0a 72 92 df 2e 51 93 25 89 a3 ea 64 02 95 b7 7e ba ff 9b 45 3c 7d 01 47 04 3e 02 3f 09 d4 f8 ff 8f e7 68 64 a4 5e 6f 15 b5 76 3d 69 00 b7 f0 f1 bb 96 90 0c b4 e9 b7 27 c3 00 32 95 23 f8 65 0f c3 dd 4f 21 ef 44 3e 44 5e 0d de 65 bb c8 a4 c0 1c 11 8c c2 74 2f 9c d6 50 cb bd 8c 4c 57 fb 12 ba cf 33 07 2d 56 95 99 f7 48 99 74 72 a0 23 bf 40 47 18 1c fa 70 42 5d 41 6a 40 f6 f6 a6 a3 98 f4 5e 13 eb fa 3d a5 1b 2c 6a c6 15 6b 04 28 02 41 f2 fa ef b6 d8 e9 2a f7 aa 96 d5 c6 84 7d f4 8f 84 09 68 4d 2f b8 a6 a9 e7 d5 cc 2f a8 97 29 04 65 86 29 f7 67 d4 3a e6 ac a1 f3 d7 50 41 fc 85 0b 3d 4d ea 9a 30 21 61 d2 ed 38 df 6c 85 98 39 4e 56 1c 62 6e 9d 76 d2 cb 86 1c 84 93 fd a8 7b 4a a9 c6 e5 6c 63 f2 9c d1 ef e3 ab 02 eb 2c b7 6a 16 10 b7 9a 3f c8 c2 e7 d0 a3 f9 ef f7 04 40 7e c3 cb 02 90 59 b9 94 8f 59 78 1a 51 d2 b7 01 da 53 8f fc 7f d1 4c 02 5c 86 c0 0a 16 97 b1 bb db a1 86 fc eb 57 06 50 00 d2 80 b9 dd da c3 70 8a ed dd c5 38 e0 00 7e 0e 11 cc f1 10 ad 8b 2e d3 1e 13 e3 31 c2 51 3a 50 9e 58 aa 9a e5 e4 61 ff 8b 51 b6 7f 3b 0e f3 c8 a4 5c 23 67 7a 52 4f 7f 30 b3 2d 9e 22 20 68 d8 0a e5 5c fc db fb 27 9c 77 82 48 98 d5 99 e1 5b fc 4b ab 65 14 c6 62 7e dd 22 ba 27 12 a0 2d cb ec 0c 4a d1 e6 ff 8f 14 b3 af 5c 53 df 9d 0e aa bb e1 19 51 2b 47 c9 ab a1 d2 3b 43 fc 40 74 fa a4 59 5a 69 ad a2 b7 30 a1 e1 55 35 1c a0 11 1d f9 9b 7e 83 bc 67 c9 20 41 c1 61 a2 af 0d af 24 04 a2 6b ff 70 57 1c f7 86 75 37 7b c1 d3 c0 95 d2 95 5e 8a 37 da b3 86 d9 99 ee 3c 6f af fb 23 da 40 b7 87 e3 8d ce 76 b5 60 de 25 54 da 47 a7 8a 37 54 de cd d1 79 05 9e 03 ff 8d d6 64 5c 5e 9c 44 cf 47 ae 80 df 89 7f 4a 60 45 07 d1 b3 94 cf 85 73 35 d9 18 8b cb 25 89 65 be 36 c5 e6 4f a3 24 16 35 b1 c2 83 3f 7b 96 cb 14 d0 aa e9 a0 d0 e3 35 7b 17 a7 97 b0 5c 99 45 c1 0d 92 20 50 75 9a 4a d5 f6 04 b6 ae 58 f0 9b 16 20 94 b8 4b 0d cd 57 c0 df 48 f6 9d b8 df b5 a8 9c 4d 38 d9 28 01 56 06 68 74 ed 16 72 62 63 fb f7 8a 10 90 45 ce 00 af 0b 81 b8 05 b1 c0 eb d5 3c 97 c5 de 4e f9 98 26 2c 9b 29 7d e2 89 d2 c2 83 b7 32 39 6c 51 7e b0 b6 bf 5e de 66 4e 45 83 ec ef 7c ea 1d 3f 2b 8d 8d 8d eb 0b 3c 4f 80 32 e7 38 4d 2d 25 53 38 00 09 e1 f2 d0 79 86 9e 49 9d 25 ae bd 71 c0 c8 54 c8 1d 90 93 44 2d d0 b0 88 d8 1b 70 6b 45 c9 bd ce 64 e4 d9 27 27 f3 d4 82 a9 ea 36 88 a3 56 7f f2 cd f5 4c eb 78 18 0c d6 4c 57 b4 b7 8d 32 d5 f9 63 c7 34 81 b7 b5 f7 1f 73 36 3d fa 1d 01 5a 3e' in l:
                #     # print('_', payload, '_')
                #     # input('done')
                #     for t in range(len(tmp_lines)):
                #         print('t:', t, " ", tmp_lines[t])
                #
                #     print(l)
                #
                #     tmp_payload = ':'.join(p for p in payload).split('17:03:03:')
                #     if tmp_payload[0] == '' or tmp_payload[0] == '  ':
                #         # print('befor: ', payload)
                #         result = ' '.join(c for c in tmp_payload[1].split(':'))
                #         result = result[5:]
                #         # input('hi')
                #     else:
                #         # print('befor: ', payload)
                #         result = ' '.join(c for c in tmp_payload[0].split(':'))
                #
                #     while result[-1] == ' ':
                #         result = result[:len(result) - 1]
                #
                #     while result[0] == ' ':
                #         result = result[1:len(result)]
                #     print(result)
                #     if '50 89 33 6a 43 c8 e3 11 61 de 2b 60 71 c4 37 20 7c 0d 8a f5 95 ad 49 0c ee e5 42 61 5d 1a 75 04 8b a1 a4 b8 2d b4 c0 43 48 f2 ba 20 dd 8c 36 5f d6 e7 a1 65 0c 53 20 e8 6b 5a 18 5b 5e a7 cb 3b ed 44 2b 6d 20 86 ee f3 ba 34 a6 61 03 20 1f 58 c6 c8 6a bb 7f 95 90 73 3d 7d 9e 59 51 59 46 2f d1 0b 51 91 2e 6a c0 16 79 e9 56 d1 a7 e8 b5 6a 8a 35 a1 66 a3 0b 9e 75 99 e3 07 25 ad 0d 8f 7d 94 18 b5 54 c8 88 b2 12 4a 34 71 c5 4b 6e 00 b5 0f 16 8c e3 ed f4 7c 3b 29 2f 20 83 ca 27 e7 45 7d b1 5d 66 73 6e ee b7 19 61 cc 95 85 8f c2 8a 60 35 0c e6 ae f9 2e c4 6d 5a f5 e4 f1 80 d8 7b d7 83 2c 3c d5 31 c6 34 e2 d3 88 0a b2 1b 0f cc fd 0a bc ce dc 44 31 27 3f 29 2d 24 ec a7 d9 e0 e3 8e 7d 3d 85 5b ec 96 e1 dd d6 29 c9 dd da e8 cc c7 e7 5e 2d 31 a2 a2 ac b1 66 3a 7c 29 1c 8d 45 c5 da c4 25 d6 68 9c 0e 52 c5 72 e5 df 22 b4 e2 f6 af 9b d3 a7 76 84 05 87 8e 96 66 7b 96 c1 be 37 cf f7 3c 4d df 0f 5b 92 48 6f fc 81 bb b9 d8 ee a7 ac 93 cb 23 51 f8 6c b6 8e 6c 8e c5 a2 7f b9 c2 a7 8e aa f4 21 48 90 3a f1 b3 02 0b ca 5b a9 a0 82 eb cb 75 a7 0b e5 02 18 7b 01 64 c7 32 11 55 89 fe c4 21 8f 42 f7 5c df 43 5a 79 bc 96 5c 2a 0a 72 92 df 2e 51 93 25 89 a3 ea 64 02 95 b7 7e ba ff 9b 45 3c 7d 01 47 04 3e 02 3f 09 d4 f8 ff 8f e7 68 64 a4 5e 6f 15 b5 76 3d 69 00 b7 f0 f1 bb 96 90 0c b4 e9 b7 27 c3 00 32 95 23 f8 65 0f c3 dd 4f 21 ef 44 3e 44 5e 0d de 65 bb c8 a4 c0 1c 11 8c c2 74 2f 9c d6 50 cb bd 8c 4c 57 fb 12 ba cf 33 07 2d 56 95 99 f7 48 99 74 72 a0 23 bf 40 47 18 1c fa 70 42 5d 41 6a 40 f6 f6 a6 a3 98 f4 5e 13 eb fa 3d a5 1b 2c 6a c6 15 6b 04 28 02 41 f2 fa ef b6 d8 e9 2a f7 aa 96 d5 c6 84 7d f4 8f 84 09 68 4d 2f b8 a6 a9 e7 d5 cc 2f a8 97 29 04 65 86 29 f7 67 d4 3a e6 ac a1 f3 d7 50 41 fc 85 0b 3d 4d ea 9a 30 21 61 d2 ed 38 df 6c 85 98 39 4e 56 1c 62 6e 9d 76 d2 cb 86 1c 84 93 fd a8 7b 4a a9 c6 e5 6c 63 f2 9c d1 ef e3 ab 02 eb 2c b7 6a 16 10 b7 9a 3f c8 c2 e7 d0 a3 f9 ef f7 04 40 7e c3 cb 02 90 59 b9 94 8f 59 78 1a 51 d2 b7 01 da 53 8f fc 7f d1 4c 02 5c 86 c0 0a 16 97 b1 bb db a1 86 fc eb 57 06 50 00 d2 80 b9 dd da c3 70 8a ed dd c5 38 e0 00 7e 0e 11 cc f1 10 ad 8b 2e d3 1e 13 e3 31 c2 51 3a 50 9e 58 aa 9a e5 e4 61 ff 8b 51 b6 7f 3b 0e f3 c8 a4 5c 23 67 7a 52 4f 7f 30 b3 2d 9e 22 20 68 d8 0a e5 5c fc db fb 27 9c 77 82 48 98 d5 99 e1 5b fc 4b ab 65 14 c6 62 7e dd 22 ba 27 12 a0 2d cb ec 0c 4a d1 e6 ff 8f 14 b3 af 5c 53 df 9d 0e aa bb e1 19 51 2b 47 c9 ab a1 d2 3b 43 fc 40 74 fa a4 59 5a 69 ad a2 b7 30 a1 e1 55 35 1c a0 11 1d f9 9b 7e 83 bc 67 c9 20 41 c1 61 a2 af 0d af 24 04 a2 6b ff 70 57 1c f7 86 75 37 7b c1 d3 c0 95 d2 95 5e 8a 37 da b3 86 d9 99 ee 3c 6f af fb 23 da 40 b7 87 e3 8d ce 76 b5 60 de 25 54 da 47 a7 8a 37 54 de cd d1 79 05 9e 03 ff 8d d6 64 5c 5e 9c 44 cf 47 ae 80 df 89 7f 4a 60 45 07 d1 b3 94 cf 85 73 35 d9 18 8b cb 25 89 65 be 36 c5 e6 4f a3 24 16 35 b1 c2 83 3f 7b 96 cb 14 d0 aa e9 a0 d0 e3 35 7b 17 a7 97 b0 5c 99 45 c1 0d 92 20 50 75 9a 4a d5 f6 04 b6 ae 58 f0 9b 16 20 94 b8 4b 0d cd 57 c0 df 48 f6 9d b8 df b5 a8 9c 4d 38 d9 28 01 56 06 68 74 ed 16 72 62 63 fb f7 8a 10 90 45 ce 00 af 0b 81 b8 05 b1 c0 eb d5 3c 97 c5 de 4e f9 98 26 2c 9b 29 7d e2 89 d2 c2 83 b7 32 39 6c 51 7e b0 b6 bf 5e de 66 4e 45 83 ec ef 7c ea 1d 3f 2b 8d 8d 8d eb 0b 3c 4f 80 32 e7 38 4d 2d 25 53 38 00 09 e1 f2 d0 79 86 9e 49 9d 25 ae bd 71 c0 c8 54 c8 1d 90 93 44 2d d0 b0 88 d8 1b 70 6b 45 c9 bd ce 64 e4 d9 27 27 f3 d4 82 a9 ea 36 88 a3 56 7f f2 cd f5 4c eb 78 18 0c d6 4c 57 b4 b7 8d 32 d5 f9 63 c7 34 81 b7 b5 f7 1f 73 36 3d fa 1d 01 5a 3e' in result:
                #         print(True)
                #     else:
                #         print(False)
                #     input('hm')
            except:
                for t in range(len(tmp_lines)):
                    print('t:', t, " ", tmp_lines[t])
        return cells

    def __init__(self, application_name, payload, decrypted_payload):
        self.application_name = application_name
        self.temp = payload
        self.payload = self.__internal_check_payload(payload)
        self.decrypted_payload = decrypted_payload

        # if '50 89 33 6a 43 c8 e3 11 61 de 2b 60 71 c4 37 20 7c 0d 8a f5 95 ad 49 0c ee e5 42 61 5d 1a 75 04 8b a1 a4 b8 2d b4 c0 43 48 f2 ba 20 dd 8c 36 5f d6 e7 a1 65 0c 53 20 e8 6b 5a 18 5b 5e a7 cb 3b ed 44 2b 6d 20 86 ee f3 ba 34 a6 61 03 20 1f 58 c6 c8 6a bb 7f 95 90 73 3d 7d 9e 59 51 59 46 2f d1 0b 51 91 2e 6a c0 16 79 e9 56 d1 a7 e8 b5 6a 8a 35 a1 66 a3 0b 9e 75 99 e3 07 25 ad 0d 8f 7d 94 18 b5 54 c8 88 b2 12 4a 34 71 c5 4b 6e 00 b5 0f 16 8c e3 ed f4 7c 3b 29 2f 20 83 ca 27 e7 45 7d b1 5d 66 73 6e ee b7 19 61 cc 95 85 8f c2 8a 60 35 0c e6 ae f9 2e c4 6d 5a f5 e4 f1 80 d8 7b d7 83 2c 3c d5 31 c6 34 e2 d3 88 0a b2 1b 0f cc fd 0a bc ce dc 44 31 27 3f 29 2d 24 ec a7 d9 e0 e3 8e 7d 3d 85 5b ec 96 e1 dd d6 29 c9 dd da e8 cc c7 e7 5e 2d 31 a2 a2 ac b1 66 3a 7c 29 1c 8d 45 c5 da c4 25 d6 68 9c 0e 52 c5 72 e5 df 22 b4 e2 f6 af 9b d3 a7 76 84 05 87 8e 96 66 7b 96 c1 be 37 cf f7 3c 4d df 0f 5b 92 48 6f fc 81 bb b9 d8 ee a7 ac 93 cb 23 51 f8 6c b6 8e 6c 8e c5 a2 7f b9 c2 a7 8e aa f4 21 48 90 3a f1 b3 02 0b ca 5b a9 a0 82 eb cb 75 a7 0b e5 02 18 7b 01 64 c7 32 11 55 89 fe c4 21 8f 42 f7 5c df 43 5a 79 bc 96 5c 2a 0a 72 92 df 2e 51 93 25 89 a3 ea 64 02 95 b7 7e ba ff 9b 45 3c 7d 01 47 04 3e 02 3f 09 d4 f8 ff 8f e7 68 64 a4 5e 6f 15 b5 76 3d 69 00 b7 f0 f1 bb 96 90 0c b4 e9 b7 27 c3 00 32 95 23 f8 65 0f c3 dd 4f 21 ef 44 3e 44 5e 0d de 65 bb c8 a4 c0 1c 11 8c c2 74 2f 9c d6 50 cb bd 8c 4c 57 fb 12 ba cf 33 07 2d 56 95 99 f7 48 99 74 72 a0 23 bf 40 47 18 1c fa 70 42 5d 41 6a 40 f6 f6 a6 a3 98 f4 5e 13 eb fa 3d a5 1b 2c 6a c6 15 6b 04 28 02 41 f2 fa ef b6 d8 e9 2a f7 aa 96 d5 c6 84 7d f4 8f 84 09 68 4d 2f b8 a6 a9 e7 d5 cc 2f a8 97 29 04 65 86 29 f7 67 d4 3a e6 ac a1 f3 d7 50 41 fc 85 0b 3d 4d ea 9a 30 21 61 d2 ed 38 df 6c 85 98 39 4e 56 1c 62 6e 9d 76 d2 cb 86 1c 84 93 fd a8 7b 4a a9 c6 e5 6c 63 f2 9c d1 ef e3 ab 02 eb 2c b7 6a 16 10 b7 9a 3f c8 c2 e7 d0 a3 f9 ef f7 04 40 7e c3 cb 02 90 59 b9 94 8f 59 78 1a 51 d2 b7 01 da 53 8f fc 7f d1 4c 02 5c 86 c0 0a 16 97 b1 bb db a1 86 fc eb 57 06 50 00 d2 80 b9 dd da c3 70 8a ed dd c5 38 e0 00 7e 0e 11 cc f1 10 ad 8b 2e d3 1e 13 e3 31 c2 51 3a 50 9e 58 aa 9a e5 e4 61 ff 8b 51 b6 7f 3b 0e f3 c8 a4 5c 23 67 7a 52 4f 7f 30 b3 2d 9e 22 20 68 d8 0a e5 5c fc db fb 27 9c 77 82 48 98 d5 99 e1 5b fc 4b ab 65 14 c6 62 7e dd 22 ba 27 12 a0 2d cb ec 0c 4a d1 e6 ff 8f 14 b3 af 5c 53 df 9d 0e aa bb e1 19 51 2b 47 c9 ab a1 d2 3b 43 fc 40 74 fa a4 59 5a 69 ad a2 b7 30 a1 e1 55 35 1c a0 11 1d f9 9b 7e 83 bc 67 c9 20 41 c1 61 a2 af 0d af 24 04 a2 6b ff 70 57 1c f7 86 75 37 7b c1 d3 c0 95 d2 95 5e 8a 37 da b3 86 d9 99 ee 3c 6f af fb 23 da 40 b7 87 e3 8d ce 76 b5 60 de 25 54 da 47 a7 8a 37 54 de cd d1 79 05 9e 03 ff 8d d6 64 5c 5e 9c 44 cf 47 ae 80 df 89 7f 4a 60 45 07 d1 b3 94 cf 85 73 35 d9 18 8b cb 25 89 65 be 36 c5 e6 4f a3 24 16 35 b1 c2 83 3f 7b 96 cb 14 d0 aa e9 a0 d0 e3 35 7b 17 a7 97 b0 5c 99 45 c1 0d 92 20 50 75 9a 4a d5 f6 04 b6 ae 58 f0 9b 16 20 94 b8 4b 0d cd 57 c0 df 48 f6 9d b8 df b5 a8 9c 4d 38 d9 28 01 56 06 68 74 ed 16 72 62 63 fb f7 8a 10 90 45 ce 00 af 0b 81 b8 05 b1 c0 eb d5 3c 97 c5 de 4e f9 98 26 2c 9b 29 7d e2 89 d2 c2 83 b7 32 39 6c 51 7e b0 b6 bf 5e de 66 4e 45 83 ec ef 7c ea 1d 3f 2b 8d 8d 8d eb 0b 3c 4f 80 32 e7 38 4d 2d 25 53 38 00 09 e1 f2 d0 79 86 9e 49 9d 25 ae bd 71 c0 c8 54 c8 1d 90 93 44 2d d0 b0 88 d8 1b 70 6b 45 c9 bd ce 64 e4 d9 27 27 f3 d4 82 a9 ea 36 88 a3 56 7f f2 cd f5 4c eb 78 18 0c d6 4c 57 b4 b7 8d 32 d5 f9 63 c7 34 81 b7 b5 f7 1f 73 36 3d fa 1d 01 5a 3e' in self.temp:
        #     print('_', self.payload, '_')
        #     input('done2')

    def get_payload(self):
        return self.payload

    def get_application_name(self):
        return self.application_name

    @staticmethod
    def __internal_check_payload(payload):
        # if '17 03 03 00 58 43 ad bf 9a b7 ad d0 c4 7e 5e' in ' '.join(p for p in payload):
        # print(payload)
        tmp_payload = ':'.join(p for p in payload).split('17:03:03:')
        if tmp_payload[0] == '' or tmp_payload[0] == '  ':
            # print('befor: ', payload)
            result = ' '.join(c for c in tmp_payload[1].split(':'))
            result = result[5:]
            # input('hi')
        else:
            # print('befor: ', payload)
            result = ' '.join(c for c in tmp_payload[0].split(':'))

        while result[-1] == ' ':
            result = result[:len(result)-1]

        while result[0] == ' ':
            result = result[1:len(result)]
        # if '17 03 03 00 58 43 ad bf 9a b7 ad d0 c4 7e 5e' in ' '.join(p for p in payload):
        #     print(result)
        return ''.join(r for r in result)

        # print(len(':'.join(p for p in payload).split('17:03:03:')))
        # tmp = payload.split('170303')
        # print(tmp)


class AppData:
    labeled = 0
    number = 0

    @staticmethod
    def label_packets(packets, payload, application_name, temp):
        AppData.number += 1
        for p in packets:
            if payload in p.get_payload():
                if application_name not in p.label:
                    p.label.append(application_name)
                print('labeled: ', application_name, '\n', p.get_payload())
                AppData.labeled += 1
                print(AppData.labeled, ' ', AppData.number)
                return
        # print('not labeled: ', application_name, '\n', payload, '\n', temp)

    def __init__(self, packet, number):
        self.packet = packet
        self.label = []
        self.number = number

    def get_payload(self):
        try:

            if self.packet.ssl != self.packet[-1]:
                temp = self.packet[-1].app_data
                return ' '.join(p for p in (self.packet.ssl.app_data + temp).split(':'))
            else:
                return ' '.join(p for p in self.packet.ssl.app_data.split(':'))
        except:
            return ' '.join(p for p in self.packet.ssl.app_data.split(':'))


class CapReader:
    def __init__(self, file_name):
        self.packets = pyshark.FileCapture(file_name)

    def get_all_packets(self):
        return self.packets

    def get_ssl_app_data_packets(self):
        result = []
        i = 1
        for p in self.packets:
            try:
                if p.ssl.app_data:
                    a = AppData(p, i)
                    # print(a.packet)
                    result.append(a)
            except:
                nothing = 1
            i += 1

        return result

# for i in dir(cap[0].tcp):
#     try:
#         print(cap[0][i])
#     except:
#         a = 10
# str = cap[7].ssl.app_data

cr = CapReader('/Users/RadNi/Desktop/Jobs/tor/labled_cell_1_2.pcap')

# print(cr.get_packet_index(cr.get_all_packets()[0]))

ssl_packets = cr.get_ssl_app_data_packets()

tmp = '43 ad bf 9a b7 ad d0 c4 7e 5e 28 58 df e0 bf d5 60 5d 3d 06 9f 2a b9 91 cb 24 d1 38 fd de 7d b8 82 3d 09 17 b6 71 e4 99 89 ed 65 7f 08 84 59 d5 0c 40 ac 3d 7f 15 20 2a 08 54 ee 27 68 15 5b 5a 00 68 1a bd 58 cc ce 2a 80 96 72 4a 4e 1e 99 d6 cc 9f b4 a4 73 23 50 1d'

# while len(tmp) > 0:
#     for s in ssl_packets:
#         if tmp in s.get_payload():
#             print(s.packet)
#             input('mhhh')
#     tmp = tmp[:len(tmp)-1]

# print(ssl_packets[0].get_payload())
# all = cr.get_all_packets()
# print(dir(all[1367][-1]))
# print(all[1367][-1])
# print(all[1367][-1] == all[1367].ssl)
# input('sfad')
for p in ssl_packets:
    if '68 4c 3c 9e 42 b4 ae 4d db 55 34 54 f5 3d 0d 06 6e a4 aa 94 52 ec be 31 97 ee 8d a8 72 4c 40 a6 f9 0d 7f c9 ab e8 52 5e bb 0e d8 de 95 87 e6 15 bb 14 23 41 7f' in p.get_payload():
        print(p.get_payload())
        input('done')

# print(' '.join(str.split(':')))
cell = Cell.parse_from_file('labled_cell_1.out')
for c in Cell.parse_from_file('labled_cell_2.out'):
    cell.append(c)
#cell.append(Cell.parse_from_file('labled_cell_2.out'))

for c in cell:
    AppData.label_packets(ssl_packets, c.get_payload(), c.get_application_name(), c.temp)

# for c in cap:
#     try:
#         print(c.ssl.app_data)
#     except:
#         a = 10

# for c in cap:
#     print(c.ip.len)
#     if c.ip.len == 1109:
#         print(c)
#
# print(dir(cap[0].ip))

fw = open('./result.out', 'a+')
for ssl in ssl_packets:
    fw.write('number: ' + str(ssl.number) + '\n\t labels: ')
    for l in ssl.label:
        fw.write(l + ' ')
    fw.write('\n')

