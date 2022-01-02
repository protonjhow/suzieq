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
class PageSessionState:
    '''Session state for status page'''
    page: str = SuzieqMainPages.STATUS
    namespace: str = ''


class StatusPage(SqGuiPage):
    '''Page for Main status page'''
    _title = 'Status'

    @property
    def add_to_menu(self):
        return True

    def build(self):
        pass

    def _create_layout(self) -> None:
        pass

    def _create_sidebar(self) -> None:
        pass

    def _sync_state(self) -> None:
        pass
