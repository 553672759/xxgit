import java.awt.*;
import java.awt.event.*;
import java.io.IOException;
import java.net.*;
import java.io.*;

public class ChatClient extends Frame{//��װ��
	
	TextField tfTxt=new TextField();
	TextArea taContent=new TextArea();
	Socket s;
	DataOutputStream dos=null;
	DataInputStream dis=null;
	private boolean bConnected=false;
	Thread tRecv=new Thread(new RecvThread());
	
	public static void main(String[] args) {
		new ChatClient().launchFrame();
		
	}
	
	//��������
	public void launchFrame(){
		setLocation(400,300);
		this.setSize(300,300);
		add(tfTxt,BorderLayout.SOUTH);
		add(taContent,BorderLayout.NORTH);
		pack();
		this.addWindowListener(new WindowAdapter(){

			@Override
			public void windowClosing(WindowEvent e) {
				disconnect();
				System.exit(0);
			}
			
		});
		tfTxt.addActionListener(new TfListener());
		setVisible(true);
		connect();
		tRecv.start();
	}
	
	//��������
	public void connect(){
		try {
			 s=new Socket("127.0.0.1",8888);
			 dos=new DataOutputStream(s.getOutputStream());
			 dis=new DataInputStream(s.getInputStream());
System.out.println("connected!");
			bConnected=true;
		} catch (UnknownHostException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	//�ر�������
	public void disconnect(){
		
			try {
				dos.close();
				dis.close();
				s.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
			
			/*
			 * �ϲ��̣߳��ر��̣߳�����������������̵߳ȴ�һ��ʱ�䣬��û��Ӧ��ֱ�ӹر�
			 */
			
		
	}
	//���ڼ����س����ڲ���
	private class TfListener implements ActionListener{

		@Override
		public void actionPerformed(ActionEvent e) {
			String str=tfTxt.getText().trim();
			//taContent.setText(str);
			tfTxt.setText("");
			try {
				dos.writeUTF(str);
				dos.flush();
				//dos.close();
			} catch (IOException e1) {
				e1.printStackTrace();
			}
		}
		
	}
	
	private class RecvThread implements Runnable{

		@Override
		public void run() {
			while(bConnected){
				String str;
				try {
					str = dis.readUTF();
					taContent.setText(taContent.getText()+str+"\n");
					System.out.println(str);
				}catch(SocketException e){
						System.out.println("�˳���");				
				}catch(EOFException e){
					System.out.println("exit!");
				}
					catch (IOException e) {
					e.printStackTrace();
				}
				
			}
		}
		
	}
}







