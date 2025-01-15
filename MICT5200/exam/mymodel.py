from django.urls import path,include
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.conf import settings
from datetime import date, timedelta
from django.db.models import Q
from simphile import jaccard_similarity
from simphile import compression_similarity
from django.contrib.auth.models import User
from exam import models as DjangoDatabse
from pdf2image import convert_from_path
import grammar as Gramformer
import torch
import pytesseract
import os
import glob



class CompareModel(DjangoDatabse):

    content_file = DjangoDatabse.Tutorials.pdf_file
    student_answer = DjangoDatabse.Answer.pdf_stu

    def pdf_to_ocr(pdfs):
        answer = []

        for pdf_path in pdfs:
            pages = convert_from_path(pdf_path, 4000)

            for pageNum,imgBlob in enumerate(pages):
                text = pytesseract.image_to_string(imgBlob,lang='eng')
                answer.append(text)
        return answer


    content = glob.glob(content_file)
    answer = glob.glob(student_answer)

    content_Text = pdf_to_ocr(content)
    answer_Text = pdf_to_ocr(answer)



    def compare_pdfs(answers,cont):
        marks = []

        for ansr in answers:
            jaccard = float(jaccard_similarity(ansr, cont))
            compression = float(compression_similarity(ansr,cont))
            total_mark = jaccard+compression/2

            percent_mark = int(total_mark*100)
            marks.append(str(20+percent_mark)+"%")

        return marks
    

    def set_seed(seed):
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
    set_seed(1212)
    gc = Gramformer(models = 1, use_gpu=False) 

    def check_grammer(influent_sentence):   
        correct_grammer = ''
        for influent_sentence in influent_sentences:
            corrected_sentences = gf.correct(influent_sentence, max_candidates=1)
            for corrected_sentence in corrected_sentences:
                answer_grammer += corrected_sentence
        return correct_grammer
    
    check_grammer_answer = check_grammer(answer_Text)


    compare_percent1 = compare_pdfs(check_grammer_answer, answer_Text)
    compare_percent2 = compare_pdfs(content_Text, answer_Text)
    percent = (compare_percent2 + compare_percent2) / 2

    def __str__(self):
            return self.percent