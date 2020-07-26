from api.apirequestmaker import CodeForcesRequestMaker

from api.return_objects.blog_entry import BlogEntry
from api.return_objects.comment import Comment
from api.return_objects.contest import Contest
from api.return_objects.hack import Hack
from api.return_objects.member import Member
from api.return_objects.party import Party
from api.return_objects.problem import Problem
from api.return_objects.problem_result import ProblemResult
from api.return_objects.problem_statistics import ProblemStatistics
from api.return_objects.ranklist_row import RanklistRow
from api.return_objects.rating_change import RatingChange
from api.return_objects.recent_action import RecentAction
from api.return_objects.submission import Submission
from api.return_objects.user import User


class Client(CodeForcesRequestMaker):


