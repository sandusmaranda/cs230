import markdown
import yaml
import dominate
import dominate.tags as tags
from dominate.util import raw
from scripts.generate_base_schedule import DISPLAY_DAYS, CLASS_DAYS, LECTURE_DAYS


def convert_md_to_html_if_multiline(txt):
    html = markdown.markdown(txt)
    if '\n' not in txt:
        assert(html[:3] == '<p>')
        assert(html[-4:] == '</p>')
        
        # remove <p> tag        
        return raw(html[3:-4])

    return raw(markdown.markdown(txt))


def main():
    with open('events.yml', 'r') as f:
        events = yaml.safe_load(f)['events']

    doc = tags.table(cls='table course_calendar')

    with doc.add(tags.tbody()):
        with tags.thead():
            header = tags.tr(cls='col_headers')
            for day in DISPLAY_DAYS:
                header += tags.th(day, scope='col')

        row = None
        cur_month = ''
        for event in events:
            if event['day-of-week'] == DISPLAY_DAYS[0]:
                row = tags.tr(cls='col_headers light_row')

            day = event.get('day-of-week', None)
            special = event.get('special', None)
            pre_class = event.get('pre-class', None)
            video = event.get('video', None)
            topic = event.get('topic', None)
            slides = event.get('slides', None)
            due = event.get('due', None)
            released = event.get('released', None)
            extra_credit = event.get('extra-credit', None)
            exam = event.get('exam', None)
            class_over = event.get('class-meetings-over', None)

            td_tags = 'normalday' if special is None else 'holiday'
            if event['month'] != cur_month:
                cur_month = event['month']
                td_tags += ' new_month'

            if class_over:
                td_tags += ' readingperiod'

            with row.add(tags.td(cls=td_tags)):
                # TODO do not hardcode this
                lab = False
                if event['day-of-week'] == 'Wednesday':           
                    lab = True
                    tags.span('Lab', cls='date_label date_label_day')
                else:
                    tags.span(event['day'], cls='date_label date_label_day')   
                    tags.span(event['month'], cls='date_label date_label_month')

                with tags.ul(cls='day_agenda'):
                    if special is not None:
                        tags.li(tags.span(special, cls='day_note'))

                    if exam is not None:
                        with tags.li():
                            tags.span('Exam:', cls='tag exam_tag')
                            tags.span(convert_md_to_html_if_multiline(exam))

                    if topic is not None:
                        with tags.li():
                            if day in LECTURE_DAYS:
                                tags.span('Topic:', cls='tag topic_tag')
                            else:
                                tags.span('Lab:', cls='tag lab_tag')
                                
                            tags.span(convert_md_to_html_if_multiline(topic))

                            if slides is not None:
                                tags.span('[')
                                tags.a('materials', href=slides, target='_blank')
                                tags.span(']')                                

                    if pre_class is not None:
                        with tags.li():
                            tags.span('Pre-Lab:' if lab else 'Pre-Class:', cls='tag preclass_tag')
                            tags.span(convert_md_to_html_if_multiline(pre_class))

                    if video is not None:
                        with tags.li():
                            tags.span('Video:', cls='tag preclass_tag')
                            tags.span(convert_md_to_html_if_multiline(video))
                            
                    if due is not None:
                        with tags.li():
                            tags.span('Due:', cls='tag due_tag')
                            tags.span(convert_md_to_html_if_multiline(due))
                        
                    if released is not None:
                        with tags.li():
                            tags.span('Released:', cls='tag released_tag')
                            tags.span(convert_md_to_html_if_multiline(released))

                    if extra_credit is not None:
                        with tags.li():
                            tags.span('Extra Credit:', cls='tag extracredit_tag')
                            tags.span(convert_md_to_html_if_multiline(extra_credit))   
                    
    with open('schedule_pre.md', 'r') as f:
        print(f.read())
        
    print(doc)

    with open('schedule_post.md', 'r') as f:
        print(f.read())
    

if __name__ == '__main__':
    main()

    
