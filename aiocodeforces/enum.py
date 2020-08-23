from enum import Enum


class CEnum(Enum):
    def __str__(self):
        return self.name


class ContestType(CEnum):
    CF = 0
    IOI = 1
    ICPC = 2


class ContestPhase(CEnum):
    BEFORE = 0
    CODING = 1
    PENDING_SYSTEM_TEST = 2
    SYSTEM_TEST = 3
    FINISHED = 4


class PartyParticipantType(CEnum):
    CONTESTANT = 0
    PRACTICE = 1
    VIRTUAL = 2
    MANAGER = 3


class ProblemType(CEnum):
    PROGRAMMING = 0
    QUESTION = 1


class SubmissionVerdict(CEnum):
    FAILED = 0
    OK = 1
    PARTIAL = 2
    COMPILATION_ERROR = 3
    RUNTIME_ERROR = 4
    WRONG_ANSWER = 5
    PRESENTATION_ERROR = 6
    TIME_LIMIT_EXCEEDED = 7
    MEMORY_LIMIT_EXCEEDED = 8
    IDLENESS_LIMIT_EXCEEDED = 9
    SECURITY_VIOLATED = 10
    CRASHED = 11
    INPUT_PREPARATION_CRASHED = 12
    CHALLENGED = 13
    SKIPPED = 14
    TESTING = 15
    REJECTED = 16


class SubmissionTestSet(CEnum):
    SAMPLES = 0
    PRETESTS = 1
    TESTS = 2
    CHALLENGES = 3
    TESTS1 = 4
    TESTS2 = 5
    TESTS3 = 6
    TESTS4 = 7
    TESTS5 = 8
    TESTS6 = 9
    TESTS7 = 10
    TESTS8 = 11
    TESTS9 = 12
    TESTS10 = 13


class HackVerdict(CEnum):
    HACK_SUCCESSFUL = 0
    HACK_UNSUCCESSFUL = 1
    INVALID_INPUT = 2
    GENERATOR_INCOMPATIBLE = 3
    GENERATOR_CRASHED = 4
    IGNORED = 5
    TESTING = 6
    OTHER = 7


class ProblemResultType(CEnum):
    PRELIMINARY = 0
    FINAL = 1
