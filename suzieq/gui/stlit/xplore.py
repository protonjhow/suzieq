from dataclasses import dataclass, field, asdict
from typing import List

import numpy as np
import pandas as pd
import altair as alt
import streamlit as st

from suzieq.gui.stlit.guiutils import (sq_gui_style, gui_get_df,
                                       SuzieqMainPages)
from suzieq.gui.stlit.pagecls import SqGuiPage
from suzieq.sqobjects import get_sqobject, get_tables


@dataclass
class XploreSessionState:
    '''Session state for Xplore page'''
    page: str = SuzieqMainPages.XPLORE.value
    namespace: str = ''
    hostname: str = ''
    start_time: str = ''
    end_time: str = ''
    table: str = ''
    view: str = 'latest'
    query: str = ''
    columns:  List[str] = field(default_factory=list)
    uniq_clicked: str = '-'
    assert_clicked: bool = False


class XplorePage(SqGuiPage):
    '''Page for exploratory analysis'''
    _title: str = SuzieqMainPages.XPLORE.value
    _state: XploreSessionState = XploreSessionState()

    @property
    def add_to_menu(self) -> bool:
        return True

    def build(self):
        pass

    def _get_state_from_url(self):
        pass

    def _create_sidebar(self) -> None:
        pass

    def _create_layout(self) -> None:
        pass

    def _render(self, layout: dict) -> None:
        pass

    def _sync_state(self) -> None:
        pass

    def _save_page_url(self) -> None:
        pass
