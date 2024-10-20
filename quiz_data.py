import json
import os

file_path = 'tin.txt'  # Đổi tên biến để tránh xung đột

if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
    with open(file_path, 'r', encoding='utf-8') as f:  # Sử dụng f thay vì file
        data = f.read()
    
    def file_process(data):
        questions = data.strip().split('Câu')
        parsed_questions = []  # Đổi tên danh sách cho rõ ràng
        
        for question in questions[1:]:
            parts = [line.strip() for line in question.strip().split('\n') if line.strip()]
            
            if len(parts) < 2:
                continue
            
            try:
                question_text = parts[0].split('.', 1)[1].strip()  # Lấy nội dung câu hỏi
            except IndexError:
                continue
            
            choices = []
            answer = None
            
            for choice in parts[1:]:
                if "*" in choice:
                    star_index = choice.index('*')
                    answer = choice[star_index + 1:].strip()  # Lưu đáp án đã chọn
                    choices.append(choice[:star_index].strip() + choice[star_index + 1:].strip())  # Kết hợp phần trước và sau '*'
                else:
                    choices.append(choice.strip())  # Thêm lựa chọn không phải đáp án đúng vào danh sách
                    
            if question_text and choices:    
                parsed_questions.append({    
                                            'question': question_text,
                                            'choices': choices,
                                            'answer': answer
                                        })
        
        return parsed_questions  # Trả về danh sách các câu hỏi đã phân tích

    quiz_data = file_process(data)  # Gọi hàm file_process với dữ liệu
    print(json.dumps(quiz_data, ensure_ascii=False, indent=2))  # In kết quả dưới dạng JSON
