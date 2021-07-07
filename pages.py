from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
from django.conf import settings
import time
import random

# class FirstWaitPage(WaitPage):
#     pass
#     group_by_arrival_time = True
#
#     def is_displayed(self):
#         return self.round_number == 1


class IntroVideo(Page):

    timeout_seconds = 120

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return {"image_path": "global/background_sabotage.jpg",
                'audio_path': 'global/sabotage1.mp3'}

    def before_next_page(self):

        # players = self.subsession.get_players()
        # for p in players:
        #     if self.participant.vars['male'] is not None:
        #         self.total_num_males= sum(p.particip)
        #
        #     self. = sum([p.finished for p in players])
        #
        # for p in self.subsession.get_players():
        #     if self.participant.vars['male'] is not None:
        #
        # [1, 'Finans Direktörlüğü'],
        # [2, 'İK Direktörlüğü'],
        # [3, 'Merkez Operasyon'],
        # [4, 'Hasanoğlan Operasyon'],
        # [5, 'Sivas Operasyon'],
        # [6, 'Tedarik Zinciri Direktörlüğü'],
        # [7, 'Ticaret Direktörlüğü'],
        # [8, 'Yozgat Operasyon'],
        # [9, 'Hazır Beton'],

        number_of_departments = 8

        random_number = []
        for i in range(0, 8):
            n = random.random()
            random_number.append(n)
        print(random_number)
        print('The size of the array:', len(random_number))

        male_percent_dept = [ 0.931034483,
                              0.875,
                              0.777777778,
                              0.52173913,
                              0.956521739,
                              0.777777778,
                              0.625,
                              0.857142857]

        #print('The percentage of males in department 7 is:', male_percent_dept[6])
        #print('Range', range(number_of_departments))

        if random_number[self.participant.vars['department']-1] < male_percent_dept[self.participant.vars['department']-1]:
            self.player.other_male = 1
            self.player.other_avatar = 'male'

        else:
            self.player.other_male = 0
            self.player.other_avatar = 'female'

        self.participant.vars['other_male'] = self.player.other_male
        self.participant.vars['other_avatar'] = self.player.other_avatar

        # for i in range(0,58):
        #
        #     if self.participant.vars['department'] == i+1 and random_number[i] < male_percent_dept[i]:
        #         self.player.other_male = 1
        #         self.player.other_avatar = 'male'
        #     else:
        #         self.player.other_male = 0
        #         self.player.other_avatar = 'female'

        print('Own department:', self.participant.vars['department'])
        print('Percentage of males in the department:',self.participant.vars['department'], 'is', male_percent_dept[self.participant.vars['department']-1])
        print('Random number:', random_number[self.participant.vars['department']-1])


        print('Own gender is:', self.participant.vars['male'])
        print('Other participant\'s gender is:', self.participant.vars['other_male'])
        print('Other participant is:', self.participant.vars['other_avatar'])


        # random_number1 = random.random()
        # random_number2 = random.random()
        # random_number3 = random.random()
        # random_number4 = random.random()
        # random_number5 = random.random()
        # random_number6 = random.random()
        # random_number7 = random.random()
        # random_number8 = random.random()
        # random_number9 = random.random()
        # random_number10 = random.random()
        # random_number11 = random.random()
        # random_number12 = random.random()
        # random_number13 = random.random()
        # random_number14 = random.random()
        # random_number15 = random.random()
        # random_number16 = random.random()
        # random_number17 = random.random()
        # random_number18 = random.random()
        # random_number19 = random.random()
        # random_number20 = random.random()
        # random_number21 = random.random()
        # random_number22 = random.random()
        # random_number23 = random.random()
        # random_number24 = random.random()
        # random_number25 = random.random()
        # random_number26 = random.random()
        # random_number27 = random.random()
        # random_number28 = random.random()
        # random_number29 = random.random()
        # random_number30 = random.random()
        # random_number31 = random.random()
        # random_number32 = random.random()
        # random_number33 = random.random()
        # random_number34 = random.random()
        # random_number35 = random.random()
        # random_number36 = random.random()
        # random_number37 = random.random()
        # random_number38 = random.random()
        # random_number39 = random.random()
        # random_number40 = random.random()
        # random_number41 = random.random()
        # random_number42 = random.random()
        # random_number43 = random.random()
        # random_number44 = random.random()
        # random_number45 = random.random()
        # random_number46 = random.random()
        # random_number47 = random.random()
        # random_number48 = random.random()
        # random_number49 = random.random()
        # random_number50 = random.random()
        # random_number51 = random.random()
        # random_number52 = random.random()
        # random_number53 = random.random()
        # random_number54 = random.random()
        # random_number55 = random.random()
        # random_number56 = random.random()
        # random_number57 = random.random()
        # random_number58 = random.random()
        #
        # male_percent_dept1 = 1
        # male_percent_dept2 = 0.5
        # male_percent_dept3 = 0.8
        # male_percent_dept4 = 1
        # male_percent_dept5 = 1
        # male_percent_dept6 = 1
        # male_percent_dept7 = 0.62
        # male_percent_dept8 = 0.77
        # male_percent_dept9 = 0.83
        # male_percent_dept10 = 0.95
        # male_percent_dept11 = 0.86
        # male_percent_dept12 = 1
        # male_percent_dept13 = 1
        # male_percent_dept14 = 0.66
        # male_percent_dept15 = 0.5
        # male_percent_dept16 = 0.5
        # male_percent_dept17 = 0.5
        # male_percent_dept18 = 1
        # male_percent_dept19 = 0.86
        # male_percent_dept20 = 0.91
        # male_percent_dept21 = 1
        # male_percent_dept22 = 1
        # male_percent_dept23 = 1
        # male_percent_dept24 = 0.5
        # male_percent_dept25 = 0.5
        # male_percent_dept26 = 0
        # male_percent_dept27 = 0
        # male_percent_dept28 = 0.71
        # male_percent_dept29 = 1
        # male_percent_dept30 = 0.91
        # male_percent_dept31 = 1
        # male_percent_dept32 = 1
        # male_percent_dept33 = 0.75
        # male_percent_dept34 = 0.33
        # male_percent_dept35 = 0.66
        # male_percent_dept36 = 1
        # male_percent_dept37 = 0.5
        # male_percent_dept38 = 1
        # male_percent_dept39 = 0.93
        # male_percent_dept40 = 1
        # male_percent_dept41 = 0.88
        # male_percent_dept42 = 0.5
        # male_percent_dept43 = 1
        # male_percent_dept44 = 1
        # male_percent_dept45 = 1
        # male_percent_dept46 = 1
        # male_percent_dept47 = 1
        # male_percent_dept48 = 0.93
        # male_percent_dept49 = 1
        # male_percent_dept50 = 0.83
        # male_percent_dept51 = 0.5
        # male_percent_dept52 = 0.8
        # male_percent_dept53 = 1
        # male_percent_dept54 = 0
        # male_percent_dept55 = 0.5
        # male_percent_dept56 = 1
        # male_percent_dept57 = 0.83
        # male_percent_dept58 = 1
        #
        # if self.participant.vars['department'] == 1:
        #     if random_number1 < male_percent_dept1:
        #         self.player.other_male = 1
        #     else:
        #         self.player.other_male = 0
        #
        # if self.participant.vars['department'] == 2:
        #     if random_number2 < male_percent_dept2:
        #         self.player.other_male = 1
        #     else:
        #         self.player.other_male = 0
        #
        # if self.participant.vars['department'] == 3:
        #     if random_number3 < male_percent_dept3:
        #         self.player.other_male = 1
        #     else:
        #         self.player.other_male = 0
        #
        # if self.participant.vars['department'] == 4:
        #     if random_number4 < male_percent_dept4:
        #         self.player.other_male = 1
        #     else:
        #         self.player.other_male = 0
        #
        # if self.participant.vars['department'] == 5:
        #     if random_number5 < male_percent_dept5:
        #         self.player.other_male = 1
        #     else:
        #         self.player.other_male = 0
        #
        # if self.participant.vars['department'] == 6:
        #     if random_number6 < male_percent_dept6:
        #         self.player.other_male = 1
        #     else:
        #         self.player.other_male = 0
        #
        # if self.participant.vars['department'] == 7:
        #     if random_number7 < male_percent_dept7:
        #         self.player.other_male = 1
        #     else:
        #         self.player.other_male = 0
        #
        # if self.participant.vars['department'] == 8:
        #     if random_number8 < male_percent_dept8:
        #         self.player.other_male = 1
        #     else:
        #         self.player.other_male = 0
        #
        # if self.participant.vars['department'] == 9:
        #     if random_number9 < male_percent_dept9:
        #         self.player.other_male = 1
        #     else:
        #         self.player.other_male = 0
        #
        # if self.participant.vars['department'] == 10:
        #     if random_number10 < male_percent_dept10:
        #         self.player.other_male = 1
        #     else:
        #         self.player.other_male = 0
        #
        #
        # if self.player.other_male==1:
        #     self.player.other_avatar = 'male'
        # elif self.player.other_male==0:
        #     self.player.other_avatar = 'female'


        # print('Random number-1:', random_number1)
        # print('Random number-2:', random_number2)
        # print('Random number-3:', random_number3)
        # print('Random number-4:', random_number4)
        # print('Random number-5:', random_number5)
        # print('Random number-6:', random_number6)
        # print('Random number-7:', random_number7)
        # print('Random number-8:', random_number8)
        # print('Random number-9:', random_number9)

        # print('Percentage of males dept-1:', male_percent_dept1)
        # print('Percentage of males dept-2:', male_percent_dept2)
        # print('Percentage of males dept-3:', male_percent_dept3)
        # print('Percentage of males dept-4:', male_percent_dept4)
        # print('Percentage of males dept-5:', male_percent_dept5)
        # print('Percentage of males dept-6:', male_percent_dept6)
        # print('Percentage of males dept-7:', male_percent_dept7)
        # print('Percentage of males dept-8:', male_percent_dept8)
        # print('Percentage of males dept-9:', male_percent_dept9)

class Start(Page):

    timeout_seconds = 15

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        # user has ret_timer seconds to complete as many pages as possible
        self.participant.vars['expiry_timestamp'] = time.time() + self.player.task_timer

    def vars_for_template(self):
        return {
            'debug': settings.DEBUG,
        }

class Task(Page):

    form_model = models.Player
    form_fields = ['user_text']
    # timeout_seconds = self.player.ret_timer # time? no, only works on specific pages

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3

    def vars_for_template(self):

        # current number of correctly done tasks
        total_payoff = 0
        for p in self.player.in_all_rounds():
            if p.payoff_score != None: 
                total_payoff += p.payoff_score

        # set up messgaes in transcription task
        if self.round_number == 1: #on very first task
            correct_last_round = "<br>"
        else: #all subsequent tasks
            if self.player.in_previous_rounds()[-1].is_correct:
                correct_last_round = "Son verdiğin cevap <font color='green'>doğru</font>"
            else: 
                correct_last_round = "Son verdiğin cevap <font color='red'>yanlış</font>"
        
        return {
            'total_payoff': round(total_payoff),
            'round_count':(self.round_number - 1),
            'debug': settings.DEBUG,
            'correct_last_round': correct_last_round,        
        }

    def before_next_page(self):
        self.player.score_round()


# class Belief(Page):
#
#     def is_displayed(self):
#         return self.round_number == Constants.num_rounds
#
#     form_model = 'player'
#     form_fields = ['belief']


# class ResultsWaitPage(WaitPage):
#
#     def is_displayed(self):
#         return self.round_number == Constants.num_rounds
#
#     def after_all_players_arrive(self):
#         self.group.set_ranks_before_sabotage()


class Sabotage(Page):

    timeout_seconds = 150

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    form_model = 'player'
    form_fields = ['sabotage']

    def vars_for_template(self):

        return {
            'own_avatar': 'global/{}.jpg'.format(self.participant.vars['own_avatar']),
            'other_avatar': 'global/{}.jpg'.format(self.participant.vars['other_avatar']),
            'audio_path': 'global/sabotage2.mp3',
        }

    # def before_next_page(self):
    #     self.player.other_male = self.player.get_others_in_group()[0].participant.vars['male']
    #     self.participant.vars['other_male'] = self.player.other_male

# 'other_avatar': 'global/{}.jpg'.format(self.player.get_others_in_group()[0].participant.vars['avatar']),


# class SabotageWaitPage(WaitPage):
#
#     def is_displayed(self):
#         return self.round_number == Constants.num_rounds
#
#     def after_all_players_arrive(self):
#         self.group.set_payoffs_after_sabotage()


class BeliefOther(Page):

    timeout_seconds = 120

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):

        return {
            'audio_path': 'global/sabotage3.mp3'
        }

    form_model = 'player'
    form_fields = ['sabotage_belief']


# class SabotageBeliefWaitPage(WaitPage):
#
#     def is_displayed(self):
#         return self.round_number == Constants.num_rounds

    # def after_all_players_arrive(self):
    #     self.group.set_belief_payoffs()


page_sequence = [
    IntroVideo,
    Start,
    Task,
    Sabotage,
    BeliefOther,
]
