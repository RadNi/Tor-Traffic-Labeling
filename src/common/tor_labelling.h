//
// Created by farid on 11/29/18.
//

#ifndef TOR_TRAFFIC_LABELING_TOR_LABELLING_H
#define TOR_TRAFFIC_LABELING_TOR_LABELLING_H

#define CHUNK_MAX_ENCRYPTED_DATA_LENGTH 10000

typedef struct buf_chunks_encrypted_data_list_struct {
    char data[CHUNK_MAX_ENCRYPTED_DATA_LENGTH];
    size_t data_length;
    struct buf_chunks_encrypted_data_list_struct* next;
} buf_chunks_encrypted_data_list;


#endif //TOR_TRAFFIC_LABELING_TOR_LABELLING_H
