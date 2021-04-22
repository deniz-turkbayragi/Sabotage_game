# -*- coding: utf-8 -*-
from __future__ import division

import random

from . import pages
from ._builtin import Bot
from .models import Constants

import random


class PlayerBot(Bot):

    def play_round(self):

        if self.subsession.round_number == 1:
            yield (pages.IntroVideo)
            yield (pages.Start)

        yield (pages.Task, {'user_text': Constants.answer_key1[self.subsession.round_number - 1]})

        if self.subsession.round_number == Constants.num_rounds:
            yield (pages.Sabotage, {'sabotage': random.randint(0,50)})
            yield (pages.BeliefOther, {'sabotage_belief': random.randint(0,50)})


