import os
import streamlit as st
import numpy as np
import pandas as pd
from enums import Status
from config import compulsory_column_names
from utils import get_current_time, filter_images_by_status, shadow_highlight_correction



st.write('Shadow highlight recorder')

df = pd.read_csv('..\data\low_contrast_all_perfect_concensus_images_v2_with_means_medians.csv')
df['processing_flag'] = np.logical_and(df.low_contrast_flag_upper_pencentile_50, df.low_contrast_flag_upper_pencentile_60_lower_percentile_30)

image_path_list = list(df[df.processing_flag == True].image_paths)

@st.cache
def read_csv_and_filter(csv_path):
    render_flag = False
    df = pd.read_csv(csv_path)
    df_column_names = list(df.columns)
    if set(compulsory_column_names).issubset(set(df_column_names)) == False:
        # st.write('Column name issue')s
        render_flag = False
    else:
        render_flag = True

    return render_flag, df


def show():

    csv_file_path = os.environ['CSV_PATH']
    render_flag, df = read_csv_and_filter(
        csv_path=csv_file_path)
    
    if render_flag:
        if "df" not in st.session_state:
            st.session_state.df = df.copy()
            # data_dict = df.T.to_dict()
            pending_df = st.session_state.df[st.session_state.df.status ==
                                             Status.pending.value]
            pending_start_index = pending_df.index[0]

            st.session_state.final_index = len(df)
            st.session_state.current_index = pending_start_index
