from dataclasses import dataclass, field, asdict
from typing import List

import numpy as np
import pandas as pd
import streamlit as st

from suzieq.gui.stlit.guiutils import (sq_gui_style, gui_get_df,
                                       SuzieqMainPages)
from suzieq.gui.stlit.pagecls import SqGuiPage
from suzieq.sqobjects import get_sqobject, get_tables


@dataclass
class PathSessionState:
    '''Session state for status page'''
    namespace: str = ''
    source: str = ''
    dest: str = ''
    start_time: str = ''
    end_time: str = ''
    show_ifnames: bool = False
    vrf: str = ''
    pathobj = None
    path_df: pd.DataFrame = None


class PathPage(SqGuiPage):
    '''Page for Path trace page'''
    _title = 'Path'
    _state = PathSessionState()
    _failed_dfs_list = []

    @property
    def add_to_menu(self) -> bool:
        return True

    def build(self):
        pass

    def _create_layout(self) -> None:
        pass

    def _create_sidebar(self) -> None:
        pass

    def _sync_state(self) -> None:
        pass
